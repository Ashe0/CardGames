class Player:
  def __init__(self,name):
    self.name = name
    self.hand = []
  
  def sort_hand(self):
    self.hand.sort(key=lambda x: x.worth,reverse = True)
  
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
      if self.hand[i].rank in ("T","J","Q","K"):
        total += 10
      #If card is Ace and Ace Logic
      elif self.hand[i].rank == "A":
        if total+11 > 21:
          total +=1
        else:
          total += 11
      #If card is #
      else:
        total += int(self.hand[i].rank)
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