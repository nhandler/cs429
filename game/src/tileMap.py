import pygame
from pygame.locals import *
from tile import *
import json

TILE_UP = -1
TILE_DOWN = -2
TILE_LEFT = -1
TILE_RIGHT = -2

map_path = "../../maps/"

class TileMap():
    height = 10
    width = 10
    BLOCK_SIZE = 60
    
    tilemapping = [[]]

    x = 0
    y = 0
    tile = None
    def __init__(self, filename):
        self.x = 0
        self.y = 0
        mapdata = json.loads(open(filename).read())
        self.tilemapping = zip(*mapdata["map"]) # A little magic to rotate the array
        self.tile = Tile(map_path, self.tilemapping[self.x][self.y])

    def update(self, player, enemy_group):
        
        (px, py) = player.isOutOfBounds(
            self.width, 
            self.height, 
            TILE_LEFT, 
            TILE_RIGHT, 
            TILE_UP, 
            TILE_DOWN
        )

        for enemy in enemy_group:
            enemy.isOutOfBounds(
                self.width,
                self.height,
                TILE_LEFT,
                TILE_RIGHT,
                TILE_UP,
                TILE_DOWN
            )

        if (px == TILE_LEFT and self.x - 1 >= 0):
            self.x -= 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y])
            player.coords = (self.width-1, py)
            return False
        elif (px == TILE_RIGHT and self.x + 1 < len(self.tilemapping)):
            self.x += 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y])
            player.coords = (0, py)
            return False
        
        if (py == TILE_UP and self.y - 1 >= 0):
            self.y -= 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y])
            player.coords = (px, self.height-1)
            return False
        elif (py == TILE_DOWN and self.y + 1 < len(self.tilemapping[0])):
            self.y += 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y])
            player.coords = (px, 0)
            return False
        
        return True

    def draw(self, surface):
        self.tile.draw_background(surface)
        self.tile.draw_foreground(surface)
        self.tile.draw_top(surface)
