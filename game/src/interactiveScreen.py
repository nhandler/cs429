import pygame
from pygame.locals import *
from screen import Screen
from state import State
from locals import *

class InteractiveScreen(Screen):
	
	def __init__(self):
		self.currLine = 0
		self.lines = []

		self.sound = pygame.mixer.Sound(MENU_OPEN)
		self.sound.play()

		self.sounds = {
            		'select': pygame.mixer.Sound(SELECT),
            		'close_menu': pygame.mixer.Sound(MENU_CLOSE),
            		'menu': pygame.mixer.Sound(MENU_OPEN),
        	}

	def getNumLines(self):
		return 0

	def render(self):
		pass

	def update(self, events):
		pass

	def interact(self, event):
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
		font = pygame.font.SysFont('monospace', size)
		textColor = (255, 255, 0)
		selectedColor = (255, 0, 0)

		i = 0
		y = ystart
		for line in self.lines:
			if i == self.currLine:
				text = font.render(line, 1, selectedColor)
			else:
				text = font.render(line, 1, textColor)
			State.screen.blit(text, (100, y))
			i += 1
			y += deltay
