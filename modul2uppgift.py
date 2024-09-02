import os
os.system("cls")

x = 7
y = 5

# sum = x + y
# sum = x - y
# sum = x * y
# sum = x / y

print (x//y) # // betyder att man delar något och sedan avrundar svaret nedåt till ett heltal
print (x % y) # % använder man för att se om det finns några rester av en division kvar (modulo)
print (x ** y) # ** betyder att man höjer upp ett tal


name = input("Skriv namn: ")
age = input("Hur gammal är du? ")


print("Välkommen " + name, "du är ", age, "år gammal")


x = int(input("x: "))
y = int(input("y: "))

print("svar", x * y)


weight = float(input("Vikt i kg: "))
height = float(input("Height in m: "))

print("bmi", weight / height ** 2)

weeks = int(input("Hur gammal är du? "))

print("du är", weeks * 52, "veckor gammal")

kg = float(input("Skriv in kg: "))

print(kg, "kg är", kg * 2.20462262, "lbs" "\n\n\n")

