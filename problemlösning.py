import os
os.system('cls')

print("Hejsan! Välkommen till gångertabells palatset!!! (apa)")



for table in range(1, 13):
    print(f"{table}: tabell")
    for factor in range(1, 11):
        print(f"{table} * {factor} = {table * factor}")


