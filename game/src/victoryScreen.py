import os
import sys
import pygame
from pygame.locals import *
from state import State
from interactiveScreen import InteractiveScreen
import gameMenuScreen

class VictoryScreenLine:
    numElements = 2

    Menu = 0
    Exit = 1

class VictoryScreen(InteractiveScreen):

    def __init__(self, w, h):
        pygame.font.init()
        self.w = w
        self.h = h
        self.font = pygame.font.SysFont("monospace", 60)
        super(VictoryScreen, self).__init__()
        self.lines = [None] * VictoryScreenLine.numElements
        self.lines[VictoryScreenLine.Menu] = 'Return to Main Menu'
        self.lines[VictoryScreenLine.Exit] = 'Exit'

    def render(self):
        temp = pygame.Surface(State.screen.get_size(), flags=pygame.SRCALPHA)
        temp.fill((0,0,0,1))
        label = self.font.render("You Win", 1, (255,255,255,1))
        (width, height) = self.font.size("You Win")
        temp.blit(label, (self.w/2 - width/2, self.h/4))
        State.screen.blit(temp, (0,0))
        super(VictoryScreen, self).displayInteractiveLines(self.h/2, 50, 50)

    def update(self, events):
        for event in events:
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.currLine == VictoryScreenLine.Menu:
                        State.push_screen(gameMenuScreen.GameMenuScreen())
                    elif self.currLine == VictoryScreenLine.Exit:
                        sys.exit(0)
                else:
                    super(VictoryScreen, self).interact(event)
                    
