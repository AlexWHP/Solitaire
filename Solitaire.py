from CardDeck import *
from Piles import *

class Solitaire:
    def __init__(self) -> None:
        self.deck = Deck()
        self.foundations = dict.fromkeys({temp: []for temp in range(4)}, Foundation())
        for i in self.foundations:
            self.foundations[i] = Foundation()
        self.tableaus = dict.fromkeys({temp: []for temp in range(7)}, None)
        for i in self.tableaus:
            self.tableaus[i] = Tableau()
        self.stock = Stock()
        
    def createGame(self):
        self.deck.shuffle()
        deck_index = 0
        # Populate the tableaus
        for i in range(len(self.tableaus)):
            cards = []
            for _ in range(i + 1):
                cards.append(self.deck.getCard(deck_index))
                deck_index += 1
            self.getTableau(i).addCards(cards)
        # Populate the stock
        self.stock.stack = self.deck.cards[deck_index:]
    
    def getTableau(self, index) -> Tableau:
        """ Returns the tableau of a specific column """
        return self.tableaus[index]
    def getTableaus(self) -> dict():
        """ Returns all of the tableaus of the game """
        return self.tableaus

    def __str__(self) -> str:
        output = ""
        tab = ""
        for tabs in self.tableaus.values():
            tab = ""
            for card in tabs.stack:
                tab += str(card) + " | "
            tab += "\n"
            output += tab
        output += "\n\n"

        tab = ""
        for card in self.stock.stack:
            tab += str(card) + " | "
        tab += "\n"
        output += tab
        return output

s = Solitaire()
s.createGame()
print(s.tableaus.values())
for tabs in s.tableaus.values():
    for card in tabs.stack:
        pass

print(s)