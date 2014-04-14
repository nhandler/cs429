import sys
import pygame
from pygame.locals import *
from screen import Screen
from interactiveScreen import InteractiveScreen
from gameScreen import GameScreen
from state import State
from locals import *

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
						State.push_screen(GameScreen())
					elif self.currLine == GameMenuScreenLine.LoadGame:
						print 'Load Game'
					elif self.currLine == GameMenuScreenLine.Exit:
						sys.exit(0)
				else:
					super(GameMenuScreen, self).interact(event)
