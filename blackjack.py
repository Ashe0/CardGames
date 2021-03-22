from deck import Deck
from card import Card

class Blackjack:
  def __init__(self,startcards):
    self.startcards = startcards
    self.blackjackdeck = Deck()

  def deal_cards(self,play1,play2):
    playlist = [play1,play2]
    for i in range(len(playlist)):
      for i in range(self.startcards):
        x = self.blackjackdeck.draw()
        self.blackjackdeck.remove(x)

  def show_play_cards(self,play1):
    for i in range(len(play1.hand)):
      play1card = Card(play1.hand[i][1],play1.hand[i][0])
      play1card.show_card(play1card.rank+play1card.suit)

  def show_dealer_cards(self,dealer):
    dealercard = Card("X","X")
    dealercard.show_card()
    for i in range(len(dealer.hand)-1):
      dealercard = Card(dealer.hand[i+1][1],dealer.hand[i+1][0])
      dealercard.show_card()
    



  def __eq__(self,obj):
    return self.startcards == obj.startcards and self.decksize == obj.decksize
  def __str__(self):
    return "Blackjack is a game with " + str(self.startcards) + " Dealt to each player and a deck size of " + str(self.decksize)