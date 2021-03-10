class Cards:

  def __init__(self,suit,rank):
    self.name = suit
    self.size = rank
  
  def translate(self,x):
    #Get the Card #
    card = ""
    if x[0] == "A":
      card = card + "Ace"
    elif x[0] == "K":
      card = card + "King"
    elif x[0] == "Q":
      card = card + "Queen"
    elif x[0] == "J":
      card = card + "Jack"
    else:
      card = card + x[0]
    #Get the Card Suit
    if x[1] == "C":
      card = card + " of Clubs"
    elif x[1] == "S":
      card = card + " of Spades"
    elif x[1] == "H":
      card = card + " of Hearts"
    elif x[1] == "D":
      card = card + " of Diamonds"
    #Return Card
    return card

  def show_card(self,x):
    print(" _________")
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
    return self.name == obj.name and int(self.size) == int(obj.size)

  def __str__(self):
    return self.name + " is a "+ int(self.size) +" sized playing card deck consisting of " + self.deck + " cards."