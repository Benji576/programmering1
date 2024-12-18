import os
os.system('cls')

albums = ["Issues", "IOWA", "Obzen", "L.D.50"]


while True:

    for album in albums:
        print(album)

    delete = int(input("Which of these would you like to delete from 0-3?: "))

    albums.pop(delete)
    
    