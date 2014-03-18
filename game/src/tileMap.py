import pygame
from pygame.locals import *
from tile import Tile
import json

map_path = "../../maps/"

class TileMap():
    BLOCK_SIZE = (60, 60)
    height = 8
    width = 8
    TILE_UP = -1
    TILE_DOWN = -2
    TILE_LEFT = -1
    TILE_RIGHT = -2

    def __init__(self, filename):
        self.x = 0
        self.y = 0
        mapdata = json.loads(open(filename).read())
        self.tilemapping = zip(*mapdata["map"]) # A little magic to rotate the array
        self.tile = Tile(map_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)

    def update(self, player, enemy_group):
        
        (px, py) = player.isOutOfBounds(
            self.width, 
            self.height, 
            TileMap.TILE_LEFT, 
            TileMap.TILE_RIGHT, 
            TileMap.TILE_UP, 
            TileMap.TILE_DOWN
        )

        for enemy in enemy_group:
            enemy.isOutOfBounds(
                self.width,
                self.height,
                TileMap.TILE_LEFT,
                TileMap.TILE_RIGHT,
                TileMap.TILE_UP,
                TileMap.TILE_DOWN
            )

        if (px == TileMap.TILE_LEFT and self.x - 1 >= 0):
            self.x -= 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)
            player.coords = (self.width-1, py)
            return False
        elif (px == TileMap.TILE_RIGHT and self.x + 1 < len(self.tilemapping)):
            self.x += 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)
            player.coords = (0, py)
            return False
        
        if (py == TileMap.TILE_UP and self.y - 1 >= 0):
            self.y -= 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)
            player.coords = (px, self.height-1)
            return False
        elif (py == TileMap.TILE_DOWN and self.y + 1 < len(self.tilemapping[0])):
            self.y += 1
            self.tile = Tile(map_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)
            player.coords = (px, 0)
            return False
        
        return True

    def draw(self, surface):
        self.tile.draw_background(surface)
        self.tile.draw_foreground(surface)
        self.tile.draw_top(surface)
