import os
from screen import Screen
import pygame
from pygame.locals import *
from interactiveScreen import InteractiveScreen
import gameScreen
from state import State, load
from locals import CURRENT_GAME_DIR, NEW_GAME_DIR, USER_SAVES_DIR

class LoadGameScreenLine:
	numElements = 1

	ReturnToMainMenu = 0

class LoadGameScreen(InteractiveScreen):
	
	def __init__(self):
		super(LoadGameScreen, self).__init__()
		self.lines = [None] * LoadGameScreenLine.numElements
		self.lines[LoadGameScreenLine.ReturnToMainMenu] = 'Return To Main Menu'
		length = len(USER_SAVES_DIR)
		for root, dirs, files in os.walk(USER_SAVES_DIR):
			line = root[length:]
			if len(line) > 0:
				self.lines.append(line)

	def render(self):
		font = pygame.font.SysFont('monospace', 50)
		black = (0, 0, 0)
		State.screen.fill(black)
		instructions = font.render('Please select your save name', 1, InteractiveScreen.textColor)
		State.screen.blit(instructions, (50, 50))
		super(LoadGameScreen, self).displayInteractiveLines(200, 50, 50)
	
	def update(self, events):
		for event in events:
			if not hasattr(event, 'key'):
				continue
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					if self.currLine == LoadGameScreenLine.ReturnToMainMenu:
						State.pop_screen()
						continue
					save_name = self.lines[self.currLine]
					load(USER_SAVES_DIR + save_name)
					State.save_name = save_name
					State.pop_screen()
					State.push_screen(gameScreen.GameScreen(CURRENT_GAME_DIR))
				else:
					super(LoadGameScreen, self).interact(event)
		
