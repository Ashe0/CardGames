from cards import Cards
from player import Player

you = Player("You")

game_list = ["Black Jack","Go Fish!"]
def main_menu():
  #print games
  for i in range(len(game_list)):
    print(str(i+1)+": " + game_list[i])
  #Get the game the player wants to play
  choiceloop = True
  while choiceloop:
    choice = int(input("What number do you want to play?\n"))
    #If number is invalid, ask again
    if choice > len(game_list):
      print("Invalid: Choose a valid number")
    #If number is valid, do not ask again
    else:
      choiceloop = False
  #Start the game the player picked
  if choice == 1:
    blackjack()
  elif choice == 2:
    gofish()
  #elif choice == 3:


def blackjack():
  print("Blackjack")
  you.show_hand()
def gofish():
  print("Go Fish")
  


main_menu()