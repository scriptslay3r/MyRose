import pygame
from pygame.locals import *
import random,time
import os

def paint():
    pygame.mixer.init()
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'Sounds', 'MacMillerCircles.mp3')
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    RES=[600,600]
    BG_COLOR=[200,200,200]

    Clock=pygame.time.Clock()

    screen=pygame.display.set_mode(RES)

    x=50
    y=50
    ax,ay=5,5

    i=random.randint(1,254)
    j=random.randint(1,254)
    k=random.randint(1,254)
    ai,aj,ak=0,0,0

    screen.fill(BG_COLOR)


    xx=0
    t=time.time()


    run=True
    while run:
        xx+=1
        #screen.fill(BG_COLOR)
        if t+4<time.time():
            print("FPS: ",xx)
            t=time.time()
            xx=0





        
        COLOR=[i,j,k]

        for event in pygame.event.get():
            if event.type==QUIT:
                run=False

        while True:
            ai=random.randint(-8,8)
            aj=random.randint(-8,8)
            ak=random.randint(-8,8)
            if (i+ai in range(5,250)) and (j+aj in range(5,250)) and (k+ak in range(5,250)):
                break
            
        i=i+ai
        j=j+aj
        k=k+ak
        

        while True:
            ay=random.randint(-10,10)
            ax=random.randint(-10,10)
            if (x+ax in range(50,550)) and (y+ay in range(50,550)):
                break
            
        x=x+ax
        y=y+ay


        

        r=24
        pygame.draw.circle(screen,COLOR,[x,y],r)

        pygame.display.flip()
        Clock.tick(60)
          
    pygame.quit()
