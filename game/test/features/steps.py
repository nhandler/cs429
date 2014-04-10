from lettuce import *
import pygame
import sys
sys.path.insert(0,'../../src')
from creature import CreatureSprite
from locals import Direction
from tile import Tile

@step('The creature is at \((\d+),\s*(\d+)\)')
def creature_at(step, x, y):
    world.TestCreature.creature = CreatureSprite('Hero.png', (int(x), int(y)), (60, 60), Direction.up)
    world.TestCreature.tile = Tile(None, None, (int(x), int(y)))

@step('I move it (\w+)')
def move_creature(step, direction):
    if direction.lower() == "up":
        world.TestCreature.creature.move(Direction.up, world.TestCreature.tile)
    elif direction.lower() == "down":
        world.TestCreature.creature.move(Direction.down, world.TestCreature.tile)
    elif direction.lower() == "right":
        world.TestCreature.creature.move(Direction.right, world.TestCreature.tile)
    elif direction.lower() == "left":
        world.TestCreature.creature.move(Direction.left, world.TestCreature.tile)
    else:
        pass

@step('It is now at \((\d+),\s*(\d+)\)')
def creature_now_at(step, x, y):
    (actual_x, actual_y) = world.TestCreature.creature.coords
    assert actual_x == int(x), \
        "Creature actually at x-coord: (%d)" % actual_x

    assert actual_y == int(y), \
        "Creature actually at y-coord: (%d)" % actual_y
