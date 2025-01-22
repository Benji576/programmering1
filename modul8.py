import os
os.system('cls')



def add(a, b):
    return a + b

a = 2        
b = 3
print(a + b)


def my_name():
    print("Benjamin")

my_name()

def my_repetition():
    return "I can repeat"

for times in range(10):
    results = my_repetition()
    print(results)
    
items = [

]

def add_cars(car_list, car):
    car_list.append(car)

def remove_cars(car_list, car):
    if car in car_list:
        car_list.pop(car)

def manage_cars(car_list, new_car, old_car):
    if old_car in car_list:
        index = car_list.index(old_car)
        car_list[index] = new_car

cars = []

while True:
    print("\nCurrent List ", cars)