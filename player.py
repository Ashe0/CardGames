class Player:
  def __init__(self,name):
    self.name = name
    self.hand = []
  
  def sort_hand(self):
    self.hand.sort(key = lambda x: int(x[2]))
  
  def remove(self,x):
    self.hand.remove(x)

  def clear_hand(self):
    self.hand = []
      
  def add_hand(self,x):
    self.hand.append(x)

  def get_total(self):
    total = 0
    for i in range(len(self.hand)):
      #If card is Face/10
      if self.hand[i][0] == ("T" or "J" or "Q" or "K"):
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

  def isbust(self):
    if self.get_total() > 21:
      return True
    return False

  def __eq__(self,obj):
    return self.name == obj.name

  def __str__(self):
    return self.name + " is a player."