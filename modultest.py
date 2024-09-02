"""
DATATYPER I PYTHON

sträng, string = "text"
heltal, integer = 1... 2... 3... 10
flyttal, float = 1.2    skriv alltid flyttal med punkt som decimal

boolesk, boolean = True/False   flagga eller av och på


deklarera / initiera

"""
#initiera (namn på variabel samt datatyp)
name = ""   #string
value = 1.3 #float
value2 = 8   #integer
value3 = 8.1 #float
check = False #boolean


import os
os.system("cls")

x = 9
y = 10

x = int(input("x: "))    #input är sträng från början - du måste typkonvertera innan du gör beräkningar
y = int(input("y: "))

print(x/y, x//y)    
print("svar", x % y)

# upphöjt gör man med **
# modulo görs med % och visar på resten av en division