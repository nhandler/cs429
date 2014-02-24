import pygame
from pygame.locals import *
from cs429.pytmx import tmxloader

class Tile():
    def __init__(self, filename):
        tmxdata = tmxloader.load_pygame(filename, pixelalpha=True)
        self.height = tmxdata.height
        self.width = tmxdata.width
        
        background_index = tmxdata.tilelayers.index(
            tmxdata.getTileLayerByName('Background'))
        self.background = []
        foreground_index = tmxdata.tilelayers.index(
            tmxdata.getTileLayerByName('Foreground'))
        self.foreground = []
        top_index = tmxdata.tilelayers.index(
            tmxdata.getTileLayerByName('Top'))
        self.top = []
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
        # TODO: Add support for entities (player and enemies)
        return bool(self.foreground[x][y])

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
