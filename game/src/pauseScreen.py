import pygame 
from inventoryScreen import InventoryScreen
from pygame.locals import *
from screen import Screen
from interactiveScreen import InteractiveScreen
from state import State

class PauseScreenLines:
	numElements = 3

	Resume = 0
	Save = 1
	Quit = 2

class PauseScreen(InteractiveScreen):
    def __init__(self, player):
	super(PauseScreen, self).__init__()
        self.health = player.health
	self.lines = [None] * PauseScreenLines.numElements
	self.lines[PauseScreenLines.Resume] = 'Resume'
	self.lines[PauseScreenLines.Save] = 'Save'
	self.lines[PauseScreenLines.Quit] = 'Quit'

    def render(self):
        monospace_font = pygame.font.SysFont('monospace', 15)
	black = (0, 0, 0)
	textColor = (255, 255, 0)
        State.screen.fill(black)
        title = monospace_font.render('Game Paused', 1, textColor)
        health = monospace_font.render('Health: {0}'.format(self.health), 1, textColor)
        State.screen.blit(title, (100, 100))
        State.screen.blit(health, (100, 110))
	
	super(PauseScreen, self).displayInteractiveLines(140, 10, 15)

    def update(self, events):
        for event in events:
            if not hasattr(event, 'key'): 
                continue
            if event.type == KEYDOWN:
                if event.key == K_p:
                    State.pop_screen()
		elif event.key == K_RETURN:
			self.sounds['select'].play()
			if self.currLine == PauseScreenLines.Resume:
				State.pop_screen()
			if self.currLine == PauseScreenLines.Save:
				print 'Save Game'
			elif self.currLine == PauseScreenLines.Quit:
				State.pop_screen()
				State.pop_screen()
		elif event.key == K_i:
		    State.push_screen(InventoryScreen())
		else:
		    super(PauseScreen, self).interact(event)
