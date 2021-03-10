from player import Player
from card import Card
from deck import Deck

you = Player("You")
print(you.hand())
you.sort_hand()
print(you.hand())


'''
you = Player("You")
ai = Player("Ai")

def main_menu():
  #Get the game the player wants to play
  choice = input("Ready to Start?\n")
  for i in range(10):
    print("\n")
  blackjack()

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
  print("-------------------\nDEALER HAND:")
  ai.show_hand()
  print(text)
  for i in range(2):
    print("\n")
  you.clear_hand()
  ai.clear_hand()
  main_menu()
      
def blackjackhands():
  print("YOUR HAND:")
  you.show_hand()
  print("DEALER HAND:")
  ai.show_card("XX")
  for i in range(len(ai.hand)-1):
    ai.show_card(ai.hand[1])




    
  
main_menu()
'''