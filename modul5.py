import os
os.system('cls')

my_variable = "2"

y = my_variable.isdigit()
print(y)



while True:
    try:  
        numbers = int(input("Skriv siffror inget annat: "))
    except:
        print("Det är inte siffror")
        continue

    if number == int:
        print(numbers)
        break
    


while True:

    word = str(input("Skriv ett ord och jag kan räkna mängden bokstäver innan yoghurten: "))
    print(len(word))
    

    stop_program = str(input("Vill du avsluta så kan du klicka 'Q': ")).upper()

    if stop_program in ['Q']:
        print("Hejdå")
        break
    else:
        continue

os.system('cls')


while True:

    length_limit = 10

    word = (input("Skriv ett ord och jag kommer kapa av det om du skriver för mycket"))
    
    if len(word) > length_limit:
        word = print(word[:length_limit] + "...")
        
    stop_program = str(input("Vill du avsluta så kan du klicka 'Q': ")).upper()

    if stop_program in ['Q']:
        print("Hejdå")
        break
    else:
        continue

os.system('cls')