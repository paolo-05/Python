#Import le Librerie
import pygame
import random

#Inizializzo Pygame
pygame.init()

#Carco le Immagini
sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load ('immagini/uccello.png')
base = pygame.image.load ('immagini/base.png')
gameover = pygame.image.load ('immagini/gameover.png')
tubo_giu = pygame.image.load ('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

#Costanti Globali
SCHERMO = pygame.display.set_mode((288, 512))
FPS = 75
VEL_AVANZ = 3
FONT = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y+210))
        SCHERMO.blit(tubo_su, (self.x, self.y-210))

    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 5
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x 
        tubi_lato_sx = self.x + tubo_giu.get_width()
        uccello_lato_su = uccelloy+tolleranza
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_sx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()

    def fra_i_tubi(self, uccello, uccellox):
        tolleranza = 5
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx = uccellox+tolleranza
        tubi_lato_dx = self.x
        tubi_lato_sx = self.x + tubo_giu.get_width()
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_sx:
            return True

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex,400))
    punti_render = FONT.render(str(punti), 1, (255,255,255))
    SCHERMO.blit(punti_render, (144,0))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti
    global fra_i_tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    punti = 0
    tubi = []
    tubi.append(tubi_classe())
    fra_i_tubi = False
    
def hai_perso():
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
              inizializza()
              ricominciamo = True
          if event.type == pygame.QUIT:
              pygame.quit()
   
#inizializo variabili
inizializza()

###ciclo pricipale###
while True:
    if basex < -45: basex = 0
    basex -= VEL_AVANZ
    # Gravità
    uccello_vely +=1
    uccelloy += uccello_vely
    #comandi
    for event in pygame.event.get():
        if ( event.type == pygame.KEYDOWN
             and event.key == pygame.K_UP ):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
    #Gestione Tubi
    max_tubix = 0
    for t in tubi:
        if t.x > max_tubix: max_tubix = t.x
    if max_tubix < 150: tubi.append(tubi_classe())
    #Collisione Uccello-Tubo
    for t in tubi:
       t.collisione(uccello, uccellox, uccelloy)
    if not fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi = True
                break
    if fra_i_tubi:
        fra_i_tubi = False
        for t in tubi:
            if t.fra_i_tubi(uccello,uccellox):
                fra_i_tubi = True
                break
        if not fra_i_tubi:
            punti += 1
    #collisione con Base
    if uccelloy > 380:
            hai_perso()
    #aggiornamento
    disegna_oggetti()
    aggiorna()