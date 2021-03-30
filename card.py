class Card:
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.worth = self.get_worth(self.rank)
    self.fullcard = self.rank+self.suit

  def get_worth(self,rank):
    face_list = ["A","K","Q","J","T"]
    if rank == "X":
      worth = 14
    elif rank not in face_list:
      worth = int(rank)-1
    else:
      worth = 13-face_list.index(rank)
    return worth

  def show_card(self):
    print(" _________")
    if self.rank == "T":
      print("|"+self.suit+"        |")
      print("|10       |")
      for i in range(3):
        print("|         |")
      print("|       10|")
      print("|________"+self.suit+"|")
    else:
      print("|"+self.suit+"        |")
      print("|"+self.rank+"        |")
      for i in range(3):
        print("|         |")
      print("|        "+self.rank+"|")
      print("|________"+self.suit+"|")

  def __eq__(self,obj):
    return self.size == obj.size and self.rank == obj.rank

  def __str__(self):
    return "This card has a suit of " + self.suit + " and a rank of " + self.rank + "."