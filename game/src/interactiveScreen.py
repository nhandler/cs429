import pygame
from pygame.locals import *
from screen import Screen
from state import State
from locals import *

class InteractiveScreen(Screen):

    textColor = (255, 255, 0)
    selectedColor = (255, 0, 0)
    
    def __init__(self):
        '''
        Initializes an InteractiveScreen

        '''
        self.currLine = 0
        self.lines = []

        self.sound = pygame.mixer.Sound(MENU_OPEN)
        self.sound.play()

        self.sounds = {
                    'select': pygame.mixer.Sound(SELECT),
                    'close_menu': pygame.mixer.Sound(MENU_CLOSE),
                    'menu': pygame.mixer.Sound(MENU_OPEN),
            }

    def render(self):
        '''
        To be defined in subclasses
        '''
        pass

    def update(self, events):
        '''
        To be defined in subclasses

        @param events - List of game events
        '''

        pass

    def interact(self, event):
        '''
        When input happens this is called to change the state of the screen

        @param event - The list of events
        '''

        if not hasattr(event, 'key'):
            return
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.sounds['select'].play()
                if self.currLine > 0:
                    self.currLine -= 1
            elif event.key == K_s:
                self.sounds['select'].play()
                if self.currLine+1 < len(self.lines):
                    self.currLine += 1

    def displayInteractiveLines(self, ystart, deltay, size):
        '''
        Displays the screens lines to the screen

        @param ystart - The starting y coordinate
        @param deltay - The change in y 
        @param size - Size of the font
        '''
        font = pygame.font.SysFont('monospace', size)

        i = 0
        y = ystart
        for line in self.lines:
            if i == self.currLine:
                text = font.render(line, 1, InteractiveScreen.selectedColor)
            else:
                text = font.render(line, 1, InteractiveScreen.textColor)
            State.screen.blit(text, (180, y))
            i += 1
            y += deltay
