
accettato = False
while accettato == False:
    print("Inserisci un voto")
    voto = int(input())
    if voto > 0 and voto <= 10:
        break
    else:
        print("Voto non valido")


if voto >= 6:
    print(f"Il Voto {voto} è sufficiente")
else:
    print(f"Il Voto {voto}")
