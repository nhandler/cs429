from gameprimatives.game import *
from gameprimatives.gameobject import *

import pygame, math, sys
from pygame.locals import *

TURN_SPEED = 5
ACCELERATION = 2
MAX_FORWARD_SPEED = 10
MAX_REVERSE_SPEED = -5

class Car(GameObject):
    speed = 0

    k_up = k_down = k_left = k_right = 0

    def __init__(self, game_state):
        self.image = pygame.image.load(game_state.resource('car.png'))
        self.position = (100, 100)

    def update(self, game_state):        

        for event in game_state.events:
            if not hasattr(event, 'key'): continue
            
            down = event.type == KEYDOWN
            if event.key == K_RIGHT: self.k_right = down * -5
            elif event.key == K_LEFT: self.k_left = down * 5
            elif event.key == K_UP: self.k_up = down * 2
            elif event.key == K_DOWN: self.k_down = down * -2

        self.speed += (self.k_up + self.k_down)
        if self.speed > MAX_FORWARD_SPEED: self.speed = MAX_FORWARD_SPEED
        if self.speed < MAX_REVERSE_SPEED: self.speed = MAX_REVERSE_SPEED
        self.rotation += (self.k_right + self.k_left)

        x, y = self.position
        rad = self.rotation * math.pi/180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        min_x = min_y = 0
        max_x, max_y = game_state.screen.get_size()
        if x < min_x: x = min_x
        if x > max_x: x = max_x
        if y < min_y: y = min_y
        if y > max_y: y = max_y
        self.position = (x,y)
