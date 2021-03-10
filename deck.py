import random
class Deck:
  def __init__(self,deck,size):
    self.size = size
    self.cards = self.makedeck(True)

  def makedeck(self,tf):
    #Create variables
    deck = []
    suits = ['S','C','H','D']
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #Loop for 1. Size, 2. Suits, 3. Numbers
    for x in range(self.size):
      for i in range(len(suits)):
        for q in range(len(numbers)):
          #Make card
          card = numbers[q]+suits[i]
          #Shuffle card into deck
          deck.append(card)
    #Shuffle deck
    if tf:
      random.shuffle(deck)
    #Return deck
    return deck

  def draw(self):
    #Pick random card
    x = self.cards[0][0]
    #Draw card from deck
    card = self.cards[x]
    #Remove card from deck
    self.cards.pop(x)
    #Return Card
    return card

  def replace(self,x):
    #add the card back to the deck
    self.deck.append(x)
    random.shuffle(self.deck)

  def __eq__(self,obj):
    return self.size == obj.size and self.cards == obj.cards

  def __str__(self):
    return "Deck with " + str(len(self.cards)) + " cards in the " + str(self.size) + "x deck."
  