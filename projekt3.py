'''
projekt3.py: Detta projekt handlar om att göra ett sten, sax, påse spel som man kan se resultat och starta ny runda/avsluta program när man vill.

__author__  = "Benjamin Wall Freyne"
__version__ = "1.0.0"
__email__   = "benjamin.wallfreyne@elev.ga.ntig.se"
'''

import os
import random
from time import sleep
from msvcrt import getwch
from colors import bcolors

def clear_screen():
   os.system('cls')


def show_start_screen():   #Definerar funktionen för en startskärm
    clear_screen()
    print("""__        __   _                            _____     
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/ \n ____    ____  ____    _   _ _   _____ ___ __  __    _  _____ _____ 
|  _ \  |  _ \/ ___|  | | | | | |_   _|_ _|  \/  |  / \|_   _| ____|
| |_) | | |_) \___ \  | | | | |   | |  | || |\/| | / _ \ | | |  _|  
|  _ < _|  __/ ___) | | |_| | |___| |  | || |  | |/ ___ \| | | |___ 
|_| \_(_)_| (_)____/   \___/|_____|_| |___|_|  |_/_/   \_\_| |_____|
""")
   
def print_instructions():
    print(bcolors.PURPLE + "\n(1)Rock, (2)Paper, (3)Scissors \n N = New round \n Q = Quit" + bcolors.DEFAULT)  #Sätter färg på text och printar instruktioner till spelet


def computer_choice():
    return random.choice(['R', 'P', 'S']) #Gör så att datorn slumpmässigt väljer en av dessa alternativ


def print_choices(player, computer):   #det här är alla val som datorn och en själv kan göra i spelet
    names = {'R':
'''
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/''',

   'P': 
'''
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/''',
    
     'S': 
'''
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/'''}
    print(f"\nYou chose\n {names[player]}")  #Spelarens val
    print(f"The Computer chose\n {names[computer]}")  #Datorns val


def winner(player, computer): #den här avgör vem som vinner
    if player == computer:
        return "draw"   #Den här gör så att om man väljer samma som datorn blir det oavgjort
    elif player == "R":
        return "lose" if computer == "P" else "win"      #Den här gör så att man förlorar om man väljer R men datorn väljer något annat än P för om den väljer P så vinner spelaren
    elif player == "S":
        return "lose" if computer == "R" else "win"      
    elif player == "P":
        return "lose" if computer == "S" else "win"
    
def print_statistics(wins, losses, draws, rounds): #Funktionen här används för att printa statistiken
    print(f"""
   -Statistics-          
   Wins: {wins}   
   Losses: {losses}
   Draws: {draws}
   Total: {rounds} rounds
""") 

def get_key(): #Funktionen här definerar vilka knappar som är användbara alla andra knappar är oanvändbara
    valid_keys = ['1', '2', '3', 'R', 'P', 'S', 'N', 'Q']
    while True:
        key = getwch().upper()
        if key in valid_keys:
            return key
        
def play(): #Funktionen här gör så att spelet startar
    wins = 0
    losses = 0
    draws = 0
    rounds = 0


    while True:

      print_instructions()
      key = get_key()

      if key in ['1', 'R']:   #de här satserna ser till så att om man klickar på 1 eller R så kommer man få valet R(Rock)
         player = 'R'
      elif key in ['2', 'P']:
         player = 'P'
      elif key in ['3', 'S']:
         player = 'S'
      elif key == 'Q':     #Om man klickar på knappen Q så avslutar man spelet med break
         print("Exitting the game")
         break
      elif key == 'N':  #Den här nollställer statistik och startar om spelet
         wins = losses = draws = rounds = 0
         print("New game started!")
         continue

      computer = computer_choice()  #Den här gör så att datorn visar det den valde
      print_choices(player, computer)  #Den här printar ut det som både spelaren och datorn valde

      result = winner(player, computer)   #Den här visar resultatet
      rounds += 1 #Den här lägger på rundor

      if result == 'win':  #Den här gör så att man får +1 på wins
         wins += 1
         print(f"{bcolors.GREEN} You won! {bcolors.DEFAULT}")  #Här är en anpassad resultat för att man vinner där texten blir grön
      elif result == 'lose':  #Den här gör så att man får +1 på losses alltså sina förluster i spelet
         losses += 1
         print(f"{bcolors.RED}You lost{bcolors.DEFAULT}")   #Här är en anpassad resultat för att man förlorar där texten blir röd
      elif result == 'draw':
         draws += 1  #Den här visar hur många gånger man har fått oavgjort
         print("Draw!")

      print_statistics(wins, losses, draws, rounds)   #Den här printar statistiken så man kan se alla resultat

if __name__ == '__main__':
   show_start_screen()  #Visar start skärmen för spelet
   sleep(2.25)   #Gör så att den väntar 2.25 sekunder innan instruktionerna printas
   play()     #Startar funktionen som spelar
