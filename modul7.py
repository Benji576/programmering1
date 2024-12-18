import os
os.system('cls')

#car = {
    #"brand": ["BMW", "Ford", "Porsche"],
    #"model": "E30 M3",
    #"year": 1990
#}

#print(car["brand"])


cars = [
    {
        "make": "Audi",
        "model": "A5",
        "color": "red"
    },
        {
        "make": "Ferrari",
        "model": "f40",
        "color": "yellow"
    }
]

while True:
    for veichle in cars:
        print(veichle)

    add = str(input("Add a car of your choice: "))

    cars.append(add)

    print(cars)

    delete = int(input("Choose one from 0-1 to delete: "))

    cars.pop(delete)