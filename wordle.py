import random, pygame, sys
pygame.init() 

WHITE = (255,255,255)
YELLOW = (255,255,102)
GREY = (211,211,211)
BLACK = (0,0,0)
GREEN = (0,255,0)
LIGHTGREEN = (153,255,204)

font = pygame.font.SysFont('Helvetica neue', 40)
bigFont = pygame.font.SysFont('Helvectia neue', 80)

youWin = bigFont.render('You Win!', True, LIGHTGREEN)
youLose = bigFont.render('You Lose!', True, LIGHTGREEN)
playAgain = bigFont.render('Play Again?', True, LIGHTGREEN)

def checkGuest(turns, word, userGuess, window):
    pass