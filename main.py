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
    use_deck.shuffle_deck()
    #Deal cards to both players
    blackjackgame = Blackjack(2)
    blackjackgame.deal_cards(you,ai,use_deck)
    #Show Both of player cards,
    print("------Player Cards------")
    blackjackgame.show_play_cards(you)
    #Hide the first dealer Card
    print("------Dealer Cards------")
    blackjackgame.show_dealer_cards(ai)
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
          main_loop = False
        print("------Player Cards------")
        blackjackgame.show_play_cards(you)
      #elif player stays:
      else:
        #end this subloop, get totals of both players
        hit_loop = False
    #Dealer Draws cards
    blackjackgame.dealer_draw_loop(ai,use_deck)
    #Give a winner
    aiscore = ai.get_total()
    youscore = you.get_total()
    if aiscore == youscore:
      print("------DRAW------")
    if aiscore > youscore:
      print("------Dealer Scored Higher------")
    if aiscore < youscore:
      print("------Player Scored Higher------")
    #Ask if the player wants to play again 
    replay = input("Do you want to play again? (y/n)\n")
    if replay == "n":
      main_loop = False
main_menu()