from GameController import *

def main():
    """ Initialising values for Solitaire """
    card_width = 80
    card_height = 140  
    card_colour = (200, 200, 200)
    tab_offset = 20
    g = GameController(card_width, card_height, card_colour, tab_offset)
main()