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
        """ Resets all variables and """
        deck = self.getDeck()
        deck.hideCards()
        deck.shuffle()
        deck_index = 0
        # Populate the tableaus
        for i in range(len(self.tableaus)):
            cards = []
            for j in range(i + 1):
                card = deck.getCard(deck_index)
                cards.append(card)
                if j == i:
                    card.reveal()
                deck_index += 1
            self.getTableau(i).setStack(cards)
        # Populate the stock and reveal the top card of it
        self.getStock().setStack(deck.getCards()[deck_index:])
        deck.getCard(-1).reveal()

    def moveCards(self, cards, origin, destination):
        """ Attempts to move the cards from the origin onto the destination """
        if destination.addCards(cards):
            origin.removeCards(cards)
    
    def getDeck(self) -> Deck():
        """  Returns the deck of cards associated with the game """
        return self.deck
    def getTableau(self, index) -> Tableau:
        """ Returns the tableau of a specific column """
        return self.tableaus[index]
    def getTableaus(self) -> dict():
        """ Returns all of the tableaus of the game """
        return self.tableaus
    def getStock(self) -> Stock:
        return self.stock

    def __str__(self) -> str:
        output = ""
        tab = ""
        for tabs in self.getTableaus().values():
            tab = ""
            for card in tabs.getStack():
                tab += str(card) + " | "
            tab += "\n"
            output += tab
        output += "\n\n"

        tab = ""
        for card in self.getStock().getStack():
            tab += str(card) + " | "
        tab += "\n"
        output += tab
        return output