import random
class Cards:

  def __init__(self,name,size):
    self.name = name
    self.size = size
    self.deck = self.makedeck()
  
  def makedeck(self):
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
    random.shuffle(deck)
    #Return deck
    return deck

  def draw(self):
    #Pick random card
    x = random.randint(1,len(self.deck))
    #Draw card from deck
    card = self.deck[x]
    #Remove card from deck
    self.deck.pop(x)
    #Return Card
    return card
  
  def replace(self,x):
    #add the card back to the deck
    self.deck.append(x)
    random.shuffle(self.deck)
  
  def translate(self,x):
    #Get the Card #
    card = ""
    if x[0] == "A":
      card = card + "Ace"
    elif x[0] == "K":
      card = card + "King"
    elif x[0] == "Q":
      card = card + "Queen"
    elif x[0] == "J":
      card = card + "Jack"
    else:
      card = card + x[0]
    #Get the Card Suit
    if x[1] == "C":
      card = card + " of Clubs"
    elif x[1] == "S":
      card = card + " of Spades"
    elif x[1] == "H":
      card = card + " of Hearts"
    elif x[1] == "D":
      card = card + " of Diamonds"
    #Return Card
    return card

  

  def __eq__(self,obj):
    return self.name == obj.name and int(self.size) == int(obj.size)

  def __str__(self):
    return self.name + " is a "+ int(self.size) +" sized playing card deck consisting of " + self.deck + " cards."