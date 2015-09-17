
import random


gameStake = 50  
cards = range(10)


class Player:
    playerID = 0
    pot = 0
    lastCard = 0
    
    def __init__(self, inputID, startingPot):
        self.playerID = inputID
        self.pot = startingPot
                

    
    def play(self, dealerCard):
        	
        dealerCard = random.choice(cards)
       
        
    def play(self, playerCard):		

        lastCard = random.choice(cards)
           

    
    def addPot(playerCard, dealerCard):    
        
        if playerCard < dealerCard:
            self.pot -= gameStake
            print 'Player '+ str(self.playerID) + ' Lost ' + str(playerCard )+ ' VS ' +str(dealerCard)
        else:
            self.pot += gameStake
            print 'Player ' + str(self.playerID) + ' Won ' + str(playerCard) +' vs ' + str(dealerCard)
    def returnPot(self):
        return self.pot
        
    def returnID(self):
        return self.plaerID


def playHand(players):
    
    for player in players:
        dealerCard = random.choice(cards)
        player.play(dealerCard)
    

def checkBalances(players):
    
    for player in players:
        print 'Player ' + str(player.playerID) + ' has $' + str(player.pot) + ' Left'
  

players = []      


for i in range(5):
    players.append(Player(i, 500))

for i in range(10):
    print ''
    print 'start game ' + str(i)
    playHand(players)


print ''
print 'game results:'
checkBalances(players)
