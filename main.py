from cards import Cards
from player import Player

you = Player("You")
ai = Player("Ai")
game_list = ["Black Jack","Go Fish!"]
def main_menu():
  #print games
  you.clear_hand()
  ai.clear_hand()
  for i in range(len(game_list)):
    print(str(i+1)+": " + game_list[i])
  #Get the game the player wants to play
  choiceloop = True
  while choiceloop:
    choice = input("What number do you want to play?\n")
    #If number is invalid, ask again
    if choice.isdigit():
      if int(choice) >= 3:
        print("Invalid: Please choose a valid number")
      else:
        choiceloop = False
    else:
        print("Invalid: Choose a valid number")
      #If number is valid, do not ask again
  #Start the game the player picked
  choice = int(choice)
  if choice == 1:
    blackjack()
  elif choice == 2:
    gofish()
  


def blackjack():
  blackjack = True
  deck = Cards("Blackjack",2)
  deck.makedeck()
  while blackjack:
    you.draw(deck,2)
    ai.draw(deck,2)
    blackjackhands()
    hitloop = True
  
    while hitloop:
      choice = input("Hit(H) or Stay(S):\n")
      if choice == "H":
        you.draw(deck,1)
      elif choice == "S":
        hitloop = False
        while ai.get_total() <= 16:
          ai.draw(deck,1)
        print("-------------------")
        ai.show_hand()
        if ai.get_total() > 21:
          game_end("DEALER BUST: Player Wins")
        elif you.get_total() == ai.get_total():
          game_end("DRAW: Dealer Wins")
        elif you.get_total() > ai.get_total():
          game_end("WIN: Player Wins")
        elif you.get_total() < ai.get_total():
          game_end("LOSS: Dealer Wins")
      else:
        print("Enter a Valid Input")
      blackjackhands()
      if you.get_total() > 21:
        game_end("BUST: Dealer Wins")
      
def game_end(text):
  print(text)
  you.clear_hand()
  ai.clear_hand()
  main_menu()
      
def blackjackhands():
  print("YOUR HAND:")
  you.show_hand()
  print("AI HAND:")
  ai.show_card("XX")
  for i in range(len(ai.hand)-1):
    ai.show_card(ai.hand[1])


def gofish():
  gofish = True
  x=0
  while gofish:
    x+=1
    print(x)
  


main_menu()