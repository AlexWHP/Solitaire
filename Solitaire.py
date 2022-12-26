from CardDeck import *
from Piles import *

class Solitaire:
    def __init__(self) -> None:
        self.deck = Deck()
        self.foundations = [Foundation()]*4
        self.tableaus = [Tableau()]*7
        self.stock = Stock()
        
    def createGame(self):
        self.deck.shuffle()
        deck_index = 0
        for i in range(len(self.tableaus)):
            cards = []
            for _ in range(i + 1):
                print(deck_index)
                cards.append(self.deck.getCard(deck_index))
                deck_index += 1
            self.tableaus[i].addCards(cards)
            print(self.tableaus[i].stack)
        print(deck_index)
s = Solitaire()
s.createGame()
for tabs in s.tableaus:
    print(len(tabs.stack))
    for card in tabs.stack:
        pass
        #print(card)
    print()