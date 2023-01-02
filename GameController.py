from Solitaire import *
from CardDeck import *
from Piles import *

import pygame

class GameController:
    def __init__(self) -> None:
        """ Generates PyGame and initialises state"""
        self.game_running = False
        terminated = False
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption('Solitaire')
        # Sets Font
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.initialiseGame()
        while not terminated:
            # Checks for events from the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminated = True
            
            # Fill the background with white
            self.screen.fill((255, 255, 255))
            # Checks if state is game running
            if self.game_running:
                self.renderGame()
            # Flip the display
            pygame.display.flip()
        # Ending the game
        pygame.quit()

    def initialiseGame(self):
        self.game = Solitaire()
        print(self.game)
        self.game_running = True

    def renderGame(self):
        game = self.getGame()
        screen = self.getScreen()
        font = self.getFont()
        game.render(pygame, screen, font)
        
    
    def getGame(self):
        return self.game
    def getScreen(self):
        return self.screen
    def getFont(self):
        return self.font

def main():
    """ Initialising values for Solitaire """
    g = GameController()
main()