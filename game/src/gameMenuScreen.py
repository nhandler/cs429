import os
import sys
import pygame
from pygame.locals import *
from Tkinter import *
from enterSaveNameGUI import EnterSaveNameGUI
from screen import Screen
from interactiveScreen import InteractiveScreen
import gameScreen
import loadGameScreen
from state import State, load
from locals import CURRENT_GAME_DIR, NEW_GAME_DIR, USER_SAVES_DIR

class GameMenuScreenLine:
    '''
    The elements that will be displayed in the game menu
    '''
    numElements = 3

    NewGame = 0
    LoadGame = 1
    Exit = 2

class GameMenuScreen(InteractiveScreen):

    def __init__(self):
        '''
        Intialize the screen for the game menu
        '''
        super(GameMenuScreen, self).__init__()
        self.lines = [None] * GameMenuScreenLine.numElements
        self.lines[GameMenuScreenLine.NewGame] = 'New Game'
        self.lines[GameMenuScreenLine.LoadGame] = 'Load Game'
        self.lines[GameMenuScreenLine.Exit] = 'Exit'
    
    def render(self):
        '''
        Renders the menu to the screen 
        '''
        title_font = pygame.font.SysFont('monospace', 65)   
        regular_font = pygame.font.SysFont('monospace', 50)
        black = (0, 0, 0)
        State.screen.fill(black)
        title = title_font.render('Really Cool Game', 1, InteractiveScreen.textColor)
        State.screen.blit(title, (25, 50))
        super(GameMenuScreen, self).displayInteractiveLines(200, 50, 50)
    
    def update(self, events):
        '''
        Updates the screen when an event happens 

        @param - list of game events
        '''
        for event in events:
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.currLine == GameMenuScreenLine.NewGame:
			gui = EnterSaveNameGUI()
			save_name = gui.saveName
			if len(save_name) <= 0:
				continue
			load(NEW_GAME_DIR)
			State.save_name = save_name
                        State.push_screen(gameScreen.GameScreen(CURRENT_GAME_DIR))
                    elif self.currLine == GameMenuScreenLine.LoadGame:
			State.push_screen(loadGameScreen.LoadGameScreen())
                    elif self.currLine == GameMenuScreenLine.Exit:
                        sys.exit(0)
                else:
                    super(GameMenuScreen, self).interact(event)
