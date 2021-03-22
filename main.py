from player import Player
from deck import Deck
from blackjack import Blackjack
from card import Card

you = Player("You")
ai = Player("Ai")
game = Blackjack(2)


def main_menu():
  #Get the game the player wants to play
  choice = input("Ready to Start?\n")
  for i in range(10):
    print("\n")
  blackjack()

def blackjack():
  pass
  #Game Loop 
  main_loop = True
  while main_loop:
    #Make Deck to Use
    use_deck = Deck()
    #Deal cards to both players
    Blackjack.deal_cards(you,ai)
    #Show Both of player cards,
    Blackjack.show_play_cards(you)
    #Hide the first dealer Card
    Blackjack.show_dealer_cards(ai)
    #Subloop
    hit_loop = True
    while hit_loop:
      #Ask The Player Hit or Stay
      hit_choice = input("Hit(H) or Stay(S)?\n")
      #If the player hits:
      if hit_choice == "H":
        pass
        #Add card to player hand
        you.add_hand(use_deck.draw())
        #If the card makes the player bust
        if you.isbust():
          print("Bust")
          #End round
        #Else:
          #Return to the start of gameloop
      #elif player stays:
      else:
        #end this subloop, get totals of both players
        hit_loop = False
    #Give a winner
    #Ask if the player wants to play again 

'''
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