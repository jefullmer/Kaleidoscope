#main.py
import pygame, sys, random
from pygame.locals import *

from Shape import Shapes

pygame.init()

screenW = 1020
screenH = 900
surf = pygame.display.set_mode((screenW, screenH))
BGColor = (25, 25, 25)
surf.fill(BGColor)

clock = pygame.time.Clock()
FPS = 60

myShapes = Shapes(surf)

def main():
    counter = 0
    sizeCount = 0
    sizeMax = 0
    select = 0
    
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if select == 0:
            sizeMax = 80
        if select == 1:
            sizeMax = 140

        if sizeCount == sizeMax:
            sizeCount = 0
            select = random.randint(0,1)
            #select = 0
            surf.fill(BGColor)
        
        if counter >= 15:
            counter = 0
            myShapes.drawSelected(select, sizeCount,
                                  (random.randint(25, 255),
                                   random.randint(25, 255),
                                   random.randint(25, 255)))
            sizeCount += 1

        pygame.display.update()
        counter += 1

main()
