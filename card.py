class Card:
  def __init__(self,rank,suit):
    self.rank = rank
    self.suit = suit

  def show_card(self):
    print("___________")
    print("| " + self.suit+"       |")
    if self.rank == "T":
      print("| 10      |")
    else:
      print("| "+self.rank+"       |")
    for i in range(3):
      print("|         |")
    if self.rank == "T":
      print("|      10 |")
    else:
      print("|       "+self.rank+" |")
    print("|_______"+self.suit+"_|")

  def __str__(self):
    return "Card with rank:"+self.rank+" and suit:" +self.suit