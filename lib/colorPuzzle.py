import pygame, sys, random 
from pygame.locals import *
pygame.init()
tickTock = pygame.time.Clock()
FPS = 30
WINLENGTH = 500
WINBREADTH = 500
BOXSIZE = 40
GAPSIZE = 7
BOARDLENGTH = 5
BOARDBREADTH = 5
XMARGIN = (WINLENGTH - (BOXSIZE + GAPSIZE) * BOARDLENGTH) / 2
YMARGIN = (WINBREADTH - (BOXSIZE + GAPSIZE) * BOARDBREADTH) / 2
assert XMARGIN > 0 and YMARGIN > 0, 'The margins can never be negetive'
#Colors---------------------(  R,   G,   B)
RED =           pygame.Color(255,   0,   0)
LIGHTRED =      pygame.Color(255, 138, 138)
GREEN =         pygame.Color(  0, 255,   0)
LIGHTGREEN =    pygame.Color(138, 255, 138)
BLUE =          pygame.Color(  0,   0, 255)
LIGHTBLUE =     pygame.Color(138, 138, 255)
BKGD =          pygame.Color(255, 255, 255)  #The yellow Color
ALLCOLORS = (RED, GREEN, BLUE, LIGHTRED, LIGHTGREEN, LIGHTBLUE)
R = G = B = 0
def getFuckingBoard():
    global R, G, B
    COLORS = ALLCOLORS[:3]
    result = []
    for x in range(BOARDLENGTH):
        col = []
        for y in range(BOARDBREADTH):
            rand = random.randint(0, 1000) % 3
            col.append(COLORS[rand])
            if rand == 0:
                R += 1
            elif rand == 1:
                G += 1
            else:
                B += 1
        result.append(col)
    return result


def showFuckingBoard():
    for x in range(BOARDLENGTH):
        for y in range(BOARDBREADTH):
            COORDINATE = getXYofBox(x, y)
            pygame.draw.rect(DISPLAY, BOARD[x][y], (COORDINATE[0], COORDINATE[1], BOXSIZE, BOXSIZE)) 

def getXYofBox(x, y):
   return (XMARGIN + x * (BOXSIZE + GAPSIZE), YMARGIN + y * (BOXSIZE + GAPSIZE))

def getBoxAtPixel(mousex, mousey):
    for x in range(BOARDLENGTH):
        for y in range(BOARDBREADTH):
            fuckinRect = pygame.Rect(XMARGIN + x * (BOXSIZE + GAPSIZE), YMARGIN + y * (BOXSIZE + GAPSIZE), BOXSIZE, BOXSIZE)
            if fuckinRect.collidepoint((mousex, mousey)):
                return (x, y)
    return (None, None)

def highLightBox(BOXX, BOXY):
    if BOARD[BOXX][BOXY] == RED:
        BOARD[BOXX][BOXY] = LIGHTRED
    elif BOARD[BOXX][BOXY] == GREEN:
       BOARD[BOXX][BOXY] = LIGHTGREEN
    elif BOARD[BOXX][BOXY] == BLUE:
        BOARD[BOXX][BOXY] = LIGHTBLUE

def changeFuckingColor(BOXX, BOXY):
    if BOARD[BOXX][BOXY] == LIGHTRED:
        BOARD[BOXX][BOXY] = LIGHTGREEN
    elif BOARD[BOXX][BOXY] == LIGHTGREEN:
        BOARD[BOXX][BOXY] = LIGHTBLUE
    elif BOARD[BOXX][BOXY] == LIGHTBLUE:
        BOARD[BOXX][BOXY] = LIGHTRED
### Mouse hover currently indicates which color to print
### Reuse this program to have three basic sqaures that will show the color of them and speak the color
def resetFuckingBoard():
    for BOXX in range(BOARDLENGTH):
        for BOXY in range(BOARDBREADTH):
            if BOARD[BOXX][BOXY] == LIGHTRED:
                BOARD[BOXX][BOXY] = RED
                print("The Color was Red")
            elif BOARD[BOXX][BOXY] == LIGHTGREEN:
                BOARD[BOXX][BOXY] = GREEN
                print("The Color was green")
            elif BOARD[BOXX][BOXY] == LIGHTBLUE:
                BOARD[BOXX][BOXY] = BLUE 
                print("The Color Is Blue")

def hasWon():
    BASE = BOARD[0][0]
    for x in range(BOARDLENGTH):
        for y in range(BOARDBREADTH):
            if BASE != BOARD[x][y]:
                return False
    return True

def wonAnimation():
    pass

def predatorTry():
   stepsR = 2 * G + B
   stepsG = 2 * B + R
   stepsB = 2 * R + G
   steps = [stepsR, stepsG, stepsB]
   steps.sort()
   return steps[0]

def main():
    global BOARD, DISPLAY
    DISPLAY = pygame.display.set_mode((WINLENGTH, WINBREADTH))
    pygame.display.set_caption("Color Puzzle")
    DISPLAY.fill(BKGD)
    BOARD = getFuckingBoard()
    predator_try = predatorTry()
    showFuckingBoard()
    pygame.display.update()
    PREVIOUS = (None, None)
    mousex, mousey = 0, 0
    while True:
        CLICKED = False
        DISPLAY.fill(BKGD)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                CLICKED = True
        BOXX, BOXY = getBoxAtPixel(mousex, mousey)
        if BOXX != None and BOXY != None:
            PREVIOUS = (BOXX, BOXY)
            highLightBox(BOXX, BOXY)
            if CLICKED:
                changeFuckingColor(BOXX, BOXY)
                highLightBox(BOXX, BOXY)
        else:
            resetFuckingBoard()

        showFuckingBoard()
        pygame.display.update()
        if hasWon():
            wonAnimation()
            print ('You Won!!!, The Predator would have done it in just %d tries' %(predator_try))
            BOARD = getFuckingBoard()
            



        
if __name__ == '__main__':
    main()
