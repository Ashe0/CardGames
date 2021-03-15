class Card:

  #suit: Aces, Spades, Clubs, Diamonds
  #rank: A, K, Q, J, 10, 9, 8, . . .
  #points: how card scored in game 
  def __init__(self, suit, rank, points):
    self.suit = suit
    self.rank = rank
    self.points = points

  def __str__(self):
    return self.rank + " of " + self.suit + " is a card worth " + self.points + " points."

#Code to test class
if __name__ == "__main__":
  king_of_spades = Card("spades", "K", 10)
  print(king_of_spades)