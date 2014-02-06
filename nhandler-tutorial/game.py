import os, sys
from random import choice, randint, uniform
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite

from creep import Creep
from vec2d import vec2d

def run_game():
	# Game parameters
	SCREEN_WIDTH = 400
	SCREEN_HEIGHT = 400
	BG_COLOR = (150, 150, 80)
	CREEP_FILENAMES = [
		('bluecreep.png', 20),
		('pinkcreep.png', 20),
		('graycreep.png', 60),
	]
	N_CREEPS = 100
	CREEP_SPEED = 0.1	# 0.1 px/ms or 100 pixels per second
	
	pygame.init()
	screen = pygame.display.set_mode(
		(SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	clock = pygame.time.Clock()
	
	# Create N_CREEPS random creeps
	creeps = []
	for i in range(N_CREEPS):
		creeps.append(Creep(screen,
							w_choice(CREEP_FILENAMES),
							(	randint(0, SCREEN_WIDTH),
								randint(0, SCREEN_HEIGHT)),
							(	choice([-1, 1]),
								choice([-1, 1])),
							CREEP_SPEED))
	# The main game loop
	while True:
	    # Limit frame speed to 50 FPS
	    time_passed = clock.tick(50)
	
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit_game()
	
	    # Redraw the background
	    screen.fill(BG_COLOR)
	
	    # Update and redraw all creeps
	    for creep in creeps:
	        creep.update(time_passed)
	        creep.blitme()
	
	    pygame.display.flip()

def exit_game():
	sys.exit()

# From http://stackoverflow.com/a/4113549
def w_choice(seq):
    total_prob = sum(item[1] for item in seq)
    chosen = uniform(0, total_prob)
    cumulative = 0
    for item, probability in seq:
        cumulative += probability
        if cumulative > chosen:
            return item

run_game()
