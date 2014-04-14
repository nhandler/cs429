import json
import pygame
import sys

sys.path.insert(0, '../../pytmx')

from pygame.locals import *
from crate import ObjectSprite
from button import ButtonSprite
from enemy import EnemySprite
from shooter import ShooterSprite
from boss import BossSprite
import tmxloader
from item import MagicShoes
from locals import Direction

class Tile():
    def __init__(self, path, num, block_size):
        self.height = 0
        self.width = 0
        self.crates = []
        self.buttons = []
        self.boss = []
        self.shooters = []
        self.enemies = []
        self.background = []
        self.foreground = []
        self.top = []

        if path and num:
            tmxdata = tmxloader.load_pygame('{0}{1}.tmx'.format(path, num), pixelalpha=True)
            self.height = tmxdata.height
            self.width = tmxdata.width
            data = json.loads(open('{0}{1}.json'.format(path, num)).read())
            items = {'None': None, 'magicShoes': MagicShoes()}
            for crate in data['crates']:
                self.crates.append(
                    ObjectSprite((crate['x'], crate['y']), block_size, items[crate['item']])
                )

            for button in data['button']:
                self.buttons.append(
                    ButtonSprite((button['x'], button['y']), block_size)
                )

            for boss in data['boss']:
                self.boss.append(
                    BossSprite((boss['x'], boss['y']), block_size, Direction.left)
                )

            for shooter in data['shooters']:
                self.shooters.append(
                    ShooterSprite((shooter['x'], shooter['y']), block_size, Direction.up)
                )

            for enemy in data['enemies']:
                self.enemies.append(
                    EnemySprite((enemy['x'], enemy['y']), block_size, Direction.up)
                )

            background_index = tmxdata.tilelayers.index(
                tmxdata.getTileLayerByName('Background'))
            foreground_index = tmxdata.tilelayers.index(
                tmxdata.getTileLayerByName('Foreground'))
            top_index = tmxdata.tilelayers.index(
                tmxdata.getTileLayerByName('Top'))
            for x in range(0, self.width):
                self.background.append([])
                self.foreground.append([])
                self.top.append([])
                for y in range(0, self.height):
                    element = tmxdata.getTileImage(x, y, background_index)
                    self.background[x].append(element if element else None)

                    element = tmxdata.getTileImage(x, y, foreground_index)
                    self.foreground[x].append(element if element else None)

                    element = tmxdata.getTileImage(x, y, top_index)
                    self.top[x].append(element if element else None)

    def is_walkable(self, x, y):
        try:
            return not bool(self.foreground[x][y])
        except IndexError:
            return True

    def _convert(self, surface, x, y):
        new_x = (x * surface.get_width()) / self.width
        new_y = (y * surface.get_height()) / self.height
        return (new_x, new_y)

    def _scale(self, element, surface):
        width = surface.get_width()
        height = surface.get_height()
        num_rows = len(self.background)
        num_columns = len(self.background[0])

        return pygame.transform.scale(
            element, (width/num_rows, height/num_columns)
        )

    def _draw(self, surface, data):
        for x, column in enumerate(data):
            for y, element in enumerate(column):
                if element:
                    surface.blit(
                        self._scale(element, surface), 
                        self._convert(surface, x, y)
                    )

    def draw_background(self, surface):
        self._draw(surface, self.background)

    def draw_foreground(self, surface):
        self._draw(surface, self.foreground)

    def draw_top(self, surface):
            self._draw(surface, self.top)
