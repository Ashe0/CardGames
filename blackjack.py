from deck import Deck
from player import Player
class Blackjack:
  def __init__(self, deck):
    self.deck = deck
  
  def show_card(self,suit,rank):
    print("__________")
    print("| " + suit+"       |")
    if rank == "T":
      print("| 10     |")
    else:
      print("| "+rank+"       |")
    for i in range(4):
      print("|        |")
      print("| " +rank+"       |")
    if rank == "T":
      print("|     10 |")
    else:
      print("|       "+rank+" |")
    print("|       " + suit+" |")
    print("|________|")

  def show_hand(self,hand,tf):
    if tf:
      for i in range(len(hand)):
        self.show_card(hand[i][0],hand[i][1])
    else:
      self.show_card("X","X")
      for i in range(len(hand)-1):
        self.show_card(hand[i+1][0],hand[i+1][1])

  def hit(self,hand,deck):
    hand.append(Deck.draw(deck))

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
      if hand[i][1] == ("K" or "Q" or "J" or "T"):
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
  
  def main(self,player,dealer):
    choice = input("Are you ready to play?")
    if choice != ("n" or "N" or "no" or "No"):
      gameloop = True
      deck = Deck.reset_deck()
      player = Player()
      dealer = Player()
      while gameloop:
        #Show Hand
        self.show_hand(player,False)
        #Show Dealer Hand
        self.show_hand(dealer,True)
        #Ask for Hit
        hitchoice = input("Hit or stay? H/S\n")
        #If hit:
        if hitchoice == "H":
          self.hit(player.hand,deck)
          #is_bust:
          if self.is_bust():
            print("BUST!")
            #End Game:
            exit()
        #If stay:
        else:
          pass
          #Add dealer cards until dealer = or > 16
          while self.get_hand_total(dealer.hand) > 16:
            self.hit(dealer.hand)
          #If dealer is_bust:
          if self.get_hand_total(dealer.hand) > 21:
            #Player Win
            print("Player Wins! Dealer Bust")
            exit()
          #If dealer_total < player_total
          if self.get_hand_total(dealer.hand) < self.get_hand_total(player.hand)
            #Player Win
            print("Player Wins! Player hand Higher")
          #If dealer_total >= player_total
            #Dealer Win
          
        


#Code to test class
if __name__ == "__main__":
  suits = ["S", "D", "C", "H"]
  ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
  point_values = [[11, 1], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
  blackjack_deck = Deck(suits, ranks, point_values)

  game = Blackjack(blackjack_deck)
  game.main()
      