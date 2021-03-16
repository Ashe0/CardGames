import random
class Deck:

  def __init__(self, suits, ranks):
    self.suits = suits
    self.ranks = ranks
    self.deck = self.reset_deck()
  
  def reset_deck(self):
    decklist = []
    for i in range(len(self.suits)):
      for q in range(len(self.ranks)):
        decklist.append(self.suits[i] + self.ranks[q])
    return decklist

  def draw(self):
    card = self.deck[0]
    self.deck.remove(card)
    return card

  def is_empty(self,deck):
    if len(deck) <= 0:
      return True
    return False

  def shuffle(self):
    random.shuffle(self.deck)
  
  def __str__(self):
    return 

#Code to test class
if __name__ == "__main__":
  suits = ["S", "D", "C", "H"]
  ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
  

  standard_deck = Deck(suits, ranks)
  print(standard_deck)
