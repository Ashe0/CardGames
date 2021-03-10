class Player:
  def __init__(self,name):
    self.name = name
    self.hand = ["AH","","","",""]
  
  def sort_hand(self):
    #order = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"1":9,"J":10,"Q":11,"K":12,"A":13,}
    #self.hand.sort(key = order x: x[0])
    #print(self.hand)
  
  def add_hand(self,x):
    self.hand.append(x)

  def remove(self,x):
    self.hand.remove(x)

  def clear_hand(self):
    self.hand = []

  def show_hand(self):
    for i in range(len(self.hand)):
      self.show_card(self.hand[i])
      
  
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