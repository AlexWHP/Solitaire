from Solitaire import *
from CardDeck import *
from Piles import *

import pygame

class CardRender(Card):
    def render():
        pass

class SolitaireRender:
    def render():
        pass

def main():
    """ Initialising values for Solitaire """
    s = Solitaire()
    s.createGame()
    print(s)
main()