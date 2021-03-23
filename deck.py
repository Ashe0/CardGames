import random
from card import Card
class Deck:
  def __init__(self):
    self.suits = ['S','C','H','D']
    self.numbers = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    self.worth = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    self.cards = self.make_deck()

  def make_deck(self):
    #Create variables
    deck = []
    #Loop for 1.Suits,2. Numbers
    for i in range(len(self.suits)):
      for q in range(len(self.numbers)):
        #Make card
        newcard = Card(self.suits[i],self.numbers[q])
        cardstr = str(newcard.rank) + newcard.suit + str(newcard.worth)
        #Shuffle card into deck
        deck.append(cardstr)
    return deck

  def shuffle_deck(self):
    random.shuffle(self.cards)

  def draw(self):
    return self.cards[0] 

  def remove(self,x):
    self.cards.remove(x)

  def __eq__(self,obj):
    return self.cards == obj.cards

  def __str__(self):
    return "Deck with " + str(len(self.cards)) + " cards in the deck"
  