from card import Card
class Player:
  def __init__(self):
    self.hand = []
  
  def show_hand(self,tf):
    if tf == False:
      for i in range(len(self.hand)):
        showcard = Card(self.hand[i][1],self.hand[i][0])
        showcard.show_card()
    else:
      showcard = Card("X","X")
      showcard.show_card()
      for i in range(len(self.hand)-1):
        showcard = Card(self.hand[i+1][1],self.hand[i+1][0])
        showcard.show_card()

  def __str__(self):
    return "This Player has " + self.hand + " in their hand"