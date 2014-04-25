import os
import sys
import pygame
from pygame.locals import *
from screen import Screen
from interactiveScreen import InteractiveScreen
import gameScreen
from state import State, load
from locals import CURRENT_GAME_DIR, NEW_GAME_DIR, USER_SAVES_DIR

class GameMenuScreenLine:
    numElements = 3

    NewGame = 0
    LoadGame = 1
    Exit = 2

class GameMenuScreen(InteractiveScreen):

    def __init__(self):
        super(GameMenuScreen, self).__init__()
        self.lines = [None] * GameMenuScreenLine.numElements
        self.lines[GameMenuScreenLine.NewGame] = 'New Game'
        self.lines[GameMenuScreenLine.LoadGame] = 'Load Game'
        self.lines[GameMenuScreenLine.Exit] = 'Exit'
    
    def render(self):
        title_font = pygame.font.SysFont('monospace', 75)   
        regular_font = pygame.font.SysFont('monospace', 50)
        black = (0, 0, 0)
        textColor = (255, 255, 0)
        selectedColor = (255, 0, 0)
        State.screen.fill(black)
        title = title_font.render('Really Cool Game', 1, textColor)
        State.screen.blit(title, (25, 50))
        super(GameMenuScreen, self).displayInteractiveLines(200, 50, 50)
    
    def update(self, events):
        for event in events:
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.currLine == GameMenuScreenLine.NewGame:
                        load(NEW_GAME_DIR)
                        State.push_screen(gameScreen.GameScreen(CURRENT_GAME_DIR))
                    elif self.currLine == GameMenuScreenLine.LoadGame:
                        save_name = raw_input('Enter name of save: ')
                        if not os.path.exists(USER_SAVES_DIR + save_name):
                            print 'Save not found!'
                        else:
                            load(USER_SAVES_DIR + save_name)
                            State.push_screen(gameScreen.GameScreen(CURRENT_GAME_DIR))
                    elif self.currLine == GameMenuScreenLine.Exit:
                        sys.exit(0)
                else:
                    super(GameMenuScreen, self).interact(event)
