class Cards:
  def __init__(self,name,size):
    self.name = name
    self.size = size
    self.deck = self.makedeck()
  
  def makedeck():
    deck = []
    suits = ['S','C','H','D']
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for x in range(self.size):
      for i in range(len(suits)):
        for q in range(len(numbers)):
          card = numbers[q]+suits[i]
          deck.append(card)
    random.shuffle(deck)
    return deck

  def draw():
    x = random.randint(1,len(deck)
    card = self.deck[x]
    deck.pop[x]
    return card

  def __eq__(self,obj):
    return self.name == obj.name and self.size == obj.size

  def __str__(self):
    return self.name + " is a "+ self.size +" sized playing card deck consisting of " + self.deck + " cards."