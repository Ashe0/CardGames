class Player:
  def __init__(self,name):
    self.name = name
    self.hand = []
  
  def draw(self,deck,num):
    for i in range(num):
      self.hand.append(deck.draw())

  def remove(self,x):
    self.hand.remove(x)

  def clear_hand(self):
    self.hand = []

  def show_hand(self):
    for i in range(len(self.hand)):
      self.show_card(self.hand[i])
      
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

  def get_total(self):
    total = 0
    for i in range(len(self.hand)):
      #If card is # 10
      if self.hand[i][0:2] == "10":
        total += int(self.hand[i][0:2])
      #If card is Face
      elif self.hand[i][0] == "K" or self.hand[i][0] == "Q" or self.hand[i][0] == "J":
        total += 10
      #If card is #
      elif self.hand[i][0] == "2" or self.hand[i][0] =="3" or self.hand[i][0] == "4" or self.hand[i][0] == "5" or self.hand[i][0] == "6" or self.hand[i][0] == "7" or self.hand[i][0] == "8" or self.hand[i][0] == "9" or self.hand[i][0] =="10":
        total += int(self.hand[i][0])
      #If card is Ace and Ace Logic
      elif self.hand[i][0] == "A":
        if total+11 > 21:
          total +=1
        else:
          total += 11
    #Return Hand Total
    return total

  def __eq__(self,obj):
    return self.name == obj.name

  def __str__(self):
    return self.name + " is a player."