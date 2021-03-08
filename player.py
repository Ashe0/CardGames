class Player:
  def __init__(self,name):
    self.name = name
    self.hand = ["AD","3H","7S","10C"]
  
  def draw(self,deck):
    self.hand.append(deck.draw())

  def show_hand(self):
    for i in range(len(self.hand)):
      self.show_card(self.hand[i])
      
  def show_card(self,x):
    print(" __________")
    if len(x) == 3:
      print("|"+x[2]+"        |")
      print("|"+x[0:2]+"       |")
    else:
      print("|"+x[1]+"        |")
      print("|"+x[0]+"        |")
    for i in range(3):
      print("|         |")
    if len(x) == 3:
      print("|       "+x[0:2]+"|")
      print("|________"+x[2]+"|")
    else:
      print("|        "+x[0]+"|")
      print("|________"+x[1]+"|")

  def __eq__(self,obj):
    return self.name == obj.name

  def __str__(self):
    return self.name + " is a player."