from lettuce import world
import pygame
import sys
import unittest
sys.path.insert(0,'../src')
from creature import CreatureSprite
from locals import Direction
from tile import Tile
from player import PlayerSprite
from state import State
from item import Item, MagicShoes

@world.absorb
class TestCreature():

    creature = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

@world.absorb
class TestBullet():

    bullet = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

@world.absorb
class TestGameScreen():

    screen = None
    player = None
    creature_collide = None
    creature_miss = None
    State.screen = None
    State.health = 0

@world.absorb
class TestPlayer():

    player = None
    item = MagicShoes()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)
