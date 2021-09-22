import pyautogui, time, pyperclip

time.sleep(5)
f = open('beemovie.txt','r')
n = 0
for word in f:
    n+=1
    print(word)
    #pyautogui.typewrite(word)
print(n)