class Deck:

  def __init__(self, suits, ranks, point_values):
    self.suits = suits
    self.ranks = ranks
    self.points_values = point_values
  
  def reset_deck(self):
    decklist = []
    for i in range(len(suits)):
      for q in range(len(ranks)):
        decklist.append(suits[i] + ranks[q])
    return decklist

  def draw(self,deck):
    card = deck[0]
    deck.remove[card]
    return card

  def is_empty(self,deck):
    if len(deck) <= 0:
      return True
    return False

  def shuffle(self,deck):
    deck.shuffle()
  
  def __str__(self):
    return 

#Code to test class
if __name__ == "__main__":
  suits = ["S", "D", "C", "H"]
  ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
  point_values = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

  standard_deck = Deck(suits, ranks, point_values)
  print(standard_deck)
