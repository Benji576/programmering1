import os 
os.system('cls')

#vilkor med ifsats:

#age = int(input("your age"))


#if age == 18:
    #print("Du är precis gammal nog")

#elif age > 18:
    #print("Du är äldre än arton")

#elif age < 15:
    #print("du är mindre än 15")

#else:
    #print("Du är mer normal")






baldur_online = True


if baldur_online:
    while True:
        try:    
            height = float(input("how tall are you in m: "))
            break
        except:
            print("Write height in numbers")
            continue

    if height >= 1.2 and height <= 1.99:
        print("You can go")
    else:
        print("You can't go")

else:
    print("Baldur is closed")



bmi_kg = True

if bmi_kg:
    while True:
        try:
            height = float(input("How tall are you in m?: "))
            weight = float(input("How much do you weight in kg?: "))
            break
        except:
            print("Write height/weight in numbers")
            continue

    if height >= 0.1 and weight >=0.1:
        print("Your BMI is:", weight / height **2)
    else:
        print("That is not possible")

else:
    print("No bmi calculator found")



rad = float(input("What is the radius of the circle?: "))

print("The circles area is:", 3.14159265359 * rad ** 2)


import random

print("Tärningarnas summa:", random.randint(2, 12))


dice = int(input("Tärning slaget: "))

rolls = 0

while rolls < dice: 
    die = random.randint(1, 6)
    print(die)
    rolls += 1