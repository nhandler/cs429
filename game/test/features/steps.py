from lettuce import *
import pygame
import sys
sys.path.insert(0,'../../src')
from creature import CreatureSprite
from bullet import BulletSprite
from locals import Direction, PLAYER_IMAGE, BULLET_IMAGE
from tile import Tile
from gameScreen import GameScreen
from player import PlayerSprite
from state import State

@step('The creature is at \((\d+),\s*(\d+)\)')
def creature_at(step, x, y):
    world.TestCreature.creature = CreatureSprite(PLAYER_IMAGE, (int(x), int(y)), (60, 60), Direction.up)
    world.TestCreature.tile = Tile(None, None, (int(x), int(y)))

@step('The player is at \((\d+),\s*(\d+)\)')
def player_at(step, x, y):
    pygame.mixer.init()
    world.TestPlayer.player = PlayerSprite((int(x), int(y)), (60, 60), Direction.down)

@step('A collision has (not)? occurred')
def collission(step, not_collision):
    if not_collision:
        assert world.TestGameScreen.screen.player_enemy_collide(world.TestGameScreen.player, world.TestCreature.creature), \
        "Expected No Collision, but got Collision"
    elif not not_collision:
        assert not world.TestGameScreen.screen.player_enemy_collide(world.TestGameScreen.player, world.TestCreature.creature), \
        "Expected Collision, but got No Collision"
    else:
        pass

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
    world.TestCreature.creature.isOutOfBounds(600, 600, -1, -2, -1, -2)

@step('It is now at \((\d+),\s*(\d+)\)')
def creature_now_at(step, x, y):
    (actual_x, actual_y) = world.TestCreature.creature.coords
    assert actual_x == int(x), \
        "Creature actually at x-coord: (%d)" % actual_x

    assert actual_y == int(y), \
        "Creature actually at y-coord: (%d)" % actual_y

@step('The bullet is at \((\d+),\s*(\d+)\) moving (\w+)')
def bullet_at(step, x, y, direction):
    if direction.lower() == "up":
        world.TestBullet.bullet = BulletSprite(BULLET_IMAGE, (int(x), int(y)), (60, 60), Direction.up)
    elif direction.lower() == "down":
        world.TestBullet.bullet = BulletSprite(BULLET_IMAGE, (int(x), int(y)), (60, 60), Direction.down)
    elif direction.lower() == "right":
        world.TestBullet.bullet = BulletSprite(BULLET_IMAGE, (int(x), int(y)), (60, 60), Direction.right)
    elif direction.lower() == "left":
        world.TestBullet.bullet = BulletSprite(BULLET_IMAGE, (int(x), int(y)), (60, 60), Direction.left)
    else:
        pass

@step('The bullet moves')
def bullet_moves(step):
    world.TestBullet.bullet.update()

@step('The bullet is now at \((\d+),\s*(\d+)\)')
def bullet_now_at(step, x, y):
    (actual_x, actual_y) = world.TestBullet.bullet.coords
    assert actual_x == int(x), \
        "Bullet actually at x-coord: (%d)" % actual_x

    assert actual_y == int(y), \
        "Bullet actually at y-coord: (%d)" % actual_y

@step('When I add an item to its inventory')
def add_item(step):
    world.TestPlayer.player.addItemToInventory(world.TestPlayer.item)

@step('Then the item is in the inventory')
def item_in_inventory(step):
    inventory = world.TestPlayer.player.inventory
    assert inventory[world.TestPlayer.item] == 1, \
        "Item not added to inventory"
