i = 0
num = input('1+1? ')
while i < 10:
    if type(num) != int:
        print("insert an integer!")
        break
    num = input(f'{num}+{num}? ')
    tot = num+num
    i += 1
