from card import Card

class Blackjack:
  def __init__(self,startcards):
    self.startcards = startcards

  def deal_cards(self,play1,play2,deck):
    playlist = [play1,play2]
    for i in range(len(playlist)):
      for q in range(self.startcards):
        x = deck.draw()
        playlist[i].add_hand(x)
        deck.remove(x)

  def show_play_cards(self,play1):
    for i in range(len(play1.hand)):
      play1card = Card(play1.hand[i][1],play1.hand[i][0])
      play1card.show_card()

  def show_dealer_cards(self,dealer):
    dealercard = Card("X","X")
    dealercard.show_card()
    for i in range(len(dealer.hand)-1):
      dealercard = Card(dealer.hand[i+1][1],dealer.hand[i+1][0])
      dealercard.show_card()

  def dealer_draw_loop(self,dealer,deck):
    deal_loop = True
    while deal_loop:
      if dealer.get_total() < 16:
        addcard = deck.draw()
        dealer.add_hand(addcard)
        deck.remove(addcard)
      else:
        deal_loop = False
    
  def __eq__(self,obj):
    return self.startcards == obj.startcards and self.decksize == obj.decksize
  def __str__(self):
    return "Blackjack is a game with " + str(self.startcards) + " Dealt to each player and a deck size of " + str(self.decksize)