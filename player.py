class Player:
  def __init__(self):
    self.hand = []
  
  def __str__(self):
    return "This Player has " + self.hand + " in their hand"