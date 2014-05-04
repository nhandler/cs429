import pygame 
from inventoryScreen import InventoryScreen
from pygame.locals import *
from screen import Screen
from interactiveScreen import InteractiveScreen
from state import State, save
from locals import USER_SAVES_DIR

class PauseScreenLines:
	'''
    The elements that will be displayed in the pause menu
    '''
	numElements = 3

	Resume = 0
	Save = 1
	Quit = 2

class PauseScreen(InteractiveScreen):
    def __init__(self, player, tileMap):
    	'''
        Intialize the screen for the pause menu
        '''
		super(PauseScreen, self).__init__()
		self.player = player
	        self.tileMap = tileMap
		self.lines = [None] * PauseScreenLines.numElements
		self.lines[PauseScreenLines.Resume] = 'Resume'
		self.lines[PauseScreenLines.Save] = 'Save'
		self.lines[PauseScreenLines.Quit] = 'Quit'

    def render(self):
    	'''
        Renders the menu to the screen 
        '''
        monospace_font = pygame.font.SysFont('monospace', 15)
		black = (0, 0, 0)
        State.screen.fill(black)
        title = monospace_font.render('Game Paused', 1, InteractiveScreen.textColor)
        health = monospace_font.render('Health: {0}'.format(self.player.health), 1, InteractiveScreen.textColor)
        lives = monospace_font.render('Lives: {0}'.format(self.player.lives), 1, InteractiveScreen.textColor)
        State.screen.blit(title, (100, 100))
        State.screen.blit(health, (100, 110))
        State.screen.blit(lives, (100, 120))
	
		super(PauseScreen, self).displayInteractiveLines(140, 10, 15)

    def update(self, events):
    	'''
        Updates the screen when an event happens 

        @param - list of game events
        '''
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
                            self.tileMap.save(self.player)
                            save(USER_SAVES_DIR + State.save_name)
			elif self.currLine == PauseScreenLines.Quit:
				State.pop_screen()
				State.pop_screen()
		elif event.key == K_i:
		    State.push_screen(InventoryScreen(self.player))
		else:
		    super(PauseScreen, self).interact(event)
