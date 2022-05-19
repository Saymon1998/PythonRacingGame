import pygame
pygame.init()
from pygame.locals import*


class Main:
    def __init__(self, x=800, y=600):
        self.xAxis = x
        self.yAxis = y
    
    def gameRunState(runState):
        while runState :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runState = False

screenSize = Main()
screenDisplay = pygame.display.set_mode((
    screenSize.xAxis, screenSize.yAxis
    ))
runState = True
Main.gameRunState(runState)

