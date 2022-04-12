from operator import le
from pickle import NONE
import random, pygame, sys
from xml.etree.ElementTree import TreeBuilder
from itertools import repeat

pygame.init() 

WHITE = (255,255,255)
YELLOW = (255,255,102)
GREY = (190,190,190)
BLACK = (0,0,0)
GREEN = (0,255,0)
LIGHTGREEN = (125,238,125)

font = pygame.font.SysFont('Helvetica neue', 40)
bigFont = pygame.font.SysFont('Helvectia neue', 70)

youWin = bigFont.render('NICE!', True, LIGHTGREEN)
youLose = bigFont.render(f'DAMN!', True, LIGHTGREEN)
playAgain = bigFont.render('Play Again?', True, LIGHTGREEN)
notValid = "NOT VALID"

def checkGuest(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColorCode = [GREY, GREY, GREY, GREY, GREY]

    for letter in range(0,5):
        if userGuess[letter] in word:
            guessColorCode[letter] = YELLOW

        if userGuess[letter] == word[letter]:
            guessColorCode[letter] = GREEN

    list(userGuess)

    for letter in range(0,5):
        renderList[letter] = font.render(userGuess[letter], True, BLACK)
        pygame.draw.rect(window, guessColorCode[letter], pygame.Rect(60 + spacing, 50 + (turns*80), 50, 50))
        window.blit(renderList[letter], (70 + spacing, 50 + (turns*80)))
        spacing +=80

    if guessColorCode == [GREEN, GREEN, GREEN, GREEN, GREEN]:
        return True
    print(guessColorCode)

    
def main():

    with open('words.txt', 'r') as f:
        WORDS = f.readlines()

    with open('guess_words.txt', 'r') as f:
        f = f.readlines()

    GUESS_WORDS = []

    for x in f[:]:
        GUESS_WORDS.append(x.strip())
        

    word = WORDS[random.randint(0, len(WORDS)-1)].upper().strip()
    print(word)

    FPS = 30
    clock = pygame.time.Clock()

    HEIGHT = 600
    WIDTH = 500

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(BLACK)

    turns = 0
    guess = ''

    for x in range(0,5):
        for y in range(0,6):
            pygame.draw.rect(window, GREY, pygame.Rect(60 + (x*80), 50 + (y*80), 50, 50), 2)

    pygame.display.set_caption("Wordl")

    win = False

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

            if event.type == pygame.KEYDOWN and event.key != pygame.K_BACKSPACE:
                guess += event.unicode.upper().strip()
                print(type(guess))
                print(len(guess))
                print(guess)

                if event.key == pygame.K_RETURN and win == True:
                    main()

                if event.key == pygame.K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_RETURN and len(guess) > 4 :
                    print('checking')
                    if guess.lower() in GUESS_WORDS:
                        win = checkGuest(turns, word, guess, window)
                        turns +=1 
                        guess = ""
                        window.fill(BLACK, (0, 500, 500, 200))
  
        window.fill(BLACK, (0, 500, 500, 200))
        renderGuess = font.render(guess, True, WHITE)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(youWin, (175,200))
            window.blit(playAgain, (120, 300))

        if turns == 6 and win != True:
            window.blit(youLose, (175,200))
            window.blit(playAgain, (120, 300))

        pygame.display.update()
        clock.tick(FPS)

main()