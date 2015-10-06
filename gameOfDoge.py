# Game of Doge

import pygame, sys, os
from pygame.locals import *
import random

# Colors (RGB)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
    
# The Grid

size = [500, 600]
window = pygame.display.set_mode(size)

width = 50
height = 50
margin = 5

for row in range(10):
    for column in range(10):
        pygame.draw.rect(window, white, [(margin+width)*column+margin,
        (margin+height)*row+margin, width, height])

pygame.init()

# Start Screen

pygame.mixer.music.load('GameofDogeSong.mp3')
pygame.mixer.music.play(-1)

startScreen = True
while startScreen == True:
    pygame.display.set_caption("Game of Doge")
    window.fill(black)
    title = pygame.image.load('realtitle.png')
    window.blit(title, (0,60))
    welcome = pygame.font.SysFont('Game of Thrones', 40)
    welcomeDisplayed = welcome.render('GAME OF DOGE', True, red)
    window.blit(welcomeDisplayed, (60,6))
    instructions = pygame.font.SysFont('Arial', 20)
    instructionsDisplayed = instructions.render('Press to begin: E for easy, M for medium, H for Hard', True, red)
    window.blit(instructionsDisplayed, (60,560))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_e:
                startScreen = False
                nyanMoves = [0, 0, 55]
            if event.key == K_m:
                startScreen = False
                nyanMoves = [0, 55, 55]
            if event.key == K_h:
                startScreen = False
                nyanMoves = [55]
    pygame.display.flip()

# In-Game Music

pygame.mixer.music.load('InGameSong.mp3')
pygame.mixer.music.play(-1)

# Title

pygame.display.set_caption("Game of Doge")

# Pictures

dogepic = pygame.image.load('doge.png')
dogex = 5
dogey = 5
window.blit(dogepic, (dogex, dogey))

coinyepic = pygame.image.load('coinye.png')
window.blit(coinyepic, (445, 5))

nyancat = pygame.image.load('nyancat.png')
nyanx = 5
nyany = 510
window.blit(nyancat, (nyanx, nyany))

# Extras

movesTaken = []

def checker(moves):
    for i in range(0, len(movesTaken)):
        if movesTaken[i] != key[i]:
            return False
    return True

filledRects = []

startPosx = 5
startPosy = 5

time = 0 # Where the timer starts from (s)
pygame.time.set_timer(USEREVENT+1, 1000) #1 second is 1000 milliseconds
points = 0

win = False
    
while True:
    window.fill( (0,0,0) )
    for row in range(10):
        for column in range(10):
            pygame.draw.rect(window, white, [(margin+width)*column+margin,
            (margin+height)*row+margin, width, height])
        
    key = ['K_DOWN', 'K_RIGHT', 'K_RIGHT', 'K_UP', 'K_RIGHT', 'K_RIGHT', 'K_DOWN', 'K_DOWN', 'K_RIGHT', 'K_RIGHT', 'K_UP', 'K_UP', 'K_RIGHT', 'K_RIGHT',
       'K_DOWN', 'K_DOWN', 'K_DOWN', 'K_LEFT', 'K_DOWN', 'K_LEFT', 'K_LEFT', 'K_DOWN', 'K_LEFT', 'K_LEFT', 'K_UP', 'K_UP', 'K_LEFT', 'K_LEFT', 'K_DOWN',
       'K_DOWN', 'K_DOWN', 'K_RIGHT', 'K_DOWN', 'K_RIGHT', 'K_RIGHT', 'K_DOWN', 'K_RIGHT', 'K_RIGHT', 'K_UP', 'K_RIGHT', 'K_RIGHT', 'K_DOWN']

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == USEREVENT+1:
            time += 1
            
        if event.type == KEYDOWN:
            points += 1
            if event.key == K_RIGHT or event.key == K_d:
                dogex += 55
                movesTaken += ['K_RIGHT']
                beep = pygame.mixer.Sound('beep.wav')
                beep.play()
                if checker(movesTaken) == False:
                    dogex = startPosx
                    dogey = startPosy
                    wrongMove = pygame.mixer.Sound('doh2.wav')
                    wrongMove.play()
                    movesTaken = []
                    nyanx += random.choice(nyanMoves)
                else:
                    filledRects += [(dogex, dogey)]      
                    
            if event.key == K_LEFT or event.key == K_a:
                dogex -= 55
                movesTaken += ['K_LEFT']
                beep = pygame.mixer.Sound('beep.wav')
                beep.play()
                if checker(movesTaken) == False:
                    wrongMove = pygame.mixer.Sound('doh2.wav')
                    wrongMove.play()
                    dogex = startPosx
                    dogey = startPosy
                    movesTaken = []
                    nyanx += random.choice(nyanMoves)
                else:
                    filledRects += [(dogex, dogey)]
                    
            if event.key == K_UP or event.key == K_w:
                dogey -= 55
                movesTaken += ['K_UP']
                beep = pygame.mixer.Sound('beep.wav')
                beep.play()
                if checker(movesTaken) == False:
                    wrongMove = pygame.mixer.Sound('doh2.wav')
                    wrongMove.play()
                    dogex = startPosx
                    dogey = startPosy
                    movesTaken = []
                    nyanx += random.choice(nyanMoves)
                else:
                    filledRects += [(dogex, dogey)]
                    points += 1
                    
            if event.key == K_DOWN or event.key == K_s:
                dogey += 55
                movesTaken += ['K_DOWN']
                beep = pygame.mixer.Sound('beep.wav')
                beep.play()
                if checker(movesTaken) == False:
                    wrongMove = pygame.mixer.Sound('doh2.wav')
                    wrongMove.play()
                    dogex = startPosx
                    dogey = startPosy
                    movesTaken = []
                    nyanx += random.choice(nyanMoves)
                else:
                    filledRects += [(dogex, dogey)]
                    points += 1

    for i in filledRects[0:]:
        pawprint = pygame.image.load('pawprint.png')
        window.blit(pawprint, i)

    finalScore = points + time

    # Bottom Display

    myFont1 = pygame.font.SysFont('Arial', 15)
    myText1 = myFont1.render('Get to the kanyecoin before the Nyan cat does! Choose your moves wisely.', True, red)
    myFont2 = pygame.font.SysFont('Arial', 15)
    myText2 = myFont2.render('Everytime you make a wrong move, Nyan moves closer (how often depends on mode)', True, red)
    window.blit(myText1, (50,555))
    window.blit(myText2, (20, 575))

    window.blit(nyancat, (nyanx, nyany))
    window.blit(dogepic, (dogex, dogey))
    window.blit(coinyepic, (445, 445))

    pygame.display.update()

    # Win or Lose
    
    if (dogex, dogey) == (445, 445):
        pygame.mixer.music.stop()
        winning = pygame.mixer.Sound('WinSong.wav')
        winning.play(-1)
        window.fill( (0,0,0) )
        gameWin = pygame.image.load('titlescreen.png')
        window.blit(gameWin, (0,0))
        currentTime = time
        finalScore = currentTime + points
        scoreFont = pygame.font.SysFont('Comic Sans MS', 50)
        scoreText = scoreFont.render('Your score was: ' + str(finalScore), True, blue)
        window.blit(scoreText, (30, 440))
        scores = pygame.image.load('scores.png')
        window.blit(scores, (0,500))
        dogey += 1
        pygame.display.update()
        win = True
        break
    
    if (nyanx, nyany) == (500, 510): # You lose
        break

# Game Over

pygame.mixer.music.stop()
pygame.mixer.music.load('NyanSong.mp3')
pygame.mixer.music.play()

while True:
    if win == True:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    gameOver = pygame.image.load('putin.jpg')
    window.blit(gameOver, (0,0))
    pygame.display.update()

while True:
    pygame.mixer.music.stop()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
