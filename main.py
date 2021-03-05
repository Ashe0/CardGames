import random














def makedeck():
  deck = []
  suits = ['S','C','H','D']
  numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  for i in range(len(suits)):
    for q in range(len(numbers)):
      card = numbers[q]+suits[i]
      deck.append(card)
  random.shuffle(deck)
  return deck

deck = makedeck()
print(deck)