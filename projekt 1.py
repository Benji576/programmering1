import os
os.system('cls')

print("VÄLKOMMEN TILL DET ULTIMATA GISSA TALET SPELET MELLAN 1 - 100!")

import random

rnumber = random.randint(1, 100)

tries = 7


while True:
    try:
        realguess = int(input("Gissa ett tal mellan 1 - 100:"))
        break
    except:
        print("Skriv med siffror tack")
        continue
    

while int(realguess)<(rnumber):
    print("Du gissade för lågt!")
    realguess = input("Gissa igen:")
    tries - 1
    continue

else:
    while int(realguess)>(rnumber):
        print("Du gissade för högt!")
        realguess = input("Gissa igen:")
        tries - 1
        continue

    

if realguess == rnumber:
    print("Du gissade rätt!!!")
