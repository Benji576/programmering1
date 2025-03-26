import os
from msvcrt import getwch
import time
os.system('cls')


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    DEFAULT = '\033[0m'

print(bcolors.CYAN + "Press any key to continue!: " + bcolors.DEFAULT)
getwch()

albums = [bcolors.GREEN +"Issues" + bcolors.DEFAULT, "IOWA", "Obzen", "L.D.50"]


while True:

    for album in albums:
        print(album)

    delete = int(input(bcolors.PURPLE + "Which of these would you like to delete from 0-3?: " + bcolors.DEFAULT))

    albums.pop(delete)

    time.sleep(1)

    os.system('cls')