from deck import Deck
from player import Player
from card import Card
suits = ["S", "D", "C", "H"]
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

class Blackjack:
  def __init__(self):
    self.deck = Deck(suits,ranks)
  
  def show_hand(self,hand,tf):
    if tf == False:
      for i in range(len(hand)):
        showcard = Card(hand[i][0],hand[i][1])
        showcard.show_card()
    else:
      showcard = Card("X","X")
      showcard.show_card()
      for i in range(len(hand)-1):
        showcard = Card(hand[i+1][0],hand[i+1][1])
        showcard.show_card()

  def hit(self,hand,deck):
    hand.append(self.deck.draw())

  def is_bust(self,hand):
    if self.get_hand_total(hand) > 21:
      return True
    return False

  def is_twenty_one(self,hand):
    if self.is_bustget_hand_total(hand) == 21:
      return True
    return False

  def get_hand_total(self,hand):
    total = 0
    test = 0
    for i in range(len(hand)):
      if hand[i][1] in ("K","Q","J","T"):
        total += 10
      elif hand[i][1] != "A":
        total += int(hand[i][1]) 
      elif hand[i][1] == "A":
        test += 1

    total += 11*test
    for i in range(test):
      if total > 21:
        total -= 10
    
    return total
  
  def main(self):
    #Ask if ready to play
    choice = input("Are you ready to play?\n")
    #If they say yes
    if choice != ("n" or "N" or "no" or "No"):
      #Set up deck
      self.deck.reset_deck()
      self.deck.shuffle()
      #set up player
      player = Player()
      dealer = Player()
      userlist = [player,dealer]
      for i in range(len(userlist)):
        for q in range(2):
          self.hit(userlist[i].hand,self.deck)
      #Game Loop
      gameloop = True
      while gameloop:
        #Show Hand
        print("Player Hand:\n")
        self.show_hand(player.hand,False)
        #Show Dealer Hand
        print("--------------------\nDealer Hand:\n")
        self.show_hand(dealer.hand,True)
        #Ask for Hit
        hitchoice = input("Hit or stay? H/S\n")
        #If hit:
        if hitchoice == "H":
          self.hit(player.hand,self.deck)
          #is_bust:
          if self.is_bust(player.hand):
            print("BUST!")
            #End Game:
            gameloop = False
            self.main()
        #If stay:
        else:
          pass
          #Add dealer cards until dealer = or > 16
          while self.get_hand_total(dealer.hand) < 16:
            self.hit(dealer.hand,self.deck)
          #If dealer is_bust:
          if self.is_bust(dealer.hand):
            #Player Win
            print("Player Wins! Dealer Bust")
            gameloop = False
            self.main()
          #If dealer_total < player_total
          elif self.get_hand_total(dealer.hand) < self.get_hand_total(player.hand):
            #Player Win
            print("Player Wins! Player Hand Higher")
            gameloop = False
            self.main()
          #If dealer_total > player_total
          elif self.get_hand_total(dealer.hand) > self.get_hand_total(player.hand):
            #Dealer Win
            print("Dealer Wins! Dealer Hand Higher")
            gameloop = False
            self.main()
          #If dealer_total = player_total
          elif self.get_hand_total(dealer.hand) == self.get_hand_total(player.hand):
            #Delaer Win
            print("Dealer Wins! Tie")
            gameloop = False
            self.main()
          
        


#Code to test class
if __name__ == "__main__":
  suits = ["S", "D", "C", "H"]
  ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
  blackjack_deck = Deck(suits, ranks)

  game = Blackjack(blackjack_deck)
  game.main()
      