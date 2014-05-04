import json
import pygame
import sys

sys.path.insert(0, '../../pytmx')

from pygame.locals import *
from crate import ObjectSprite
from button import ButtonSprite
from gate import GateSprite
from enemy import EnemySprite
from shooter import ShooterSprite
from boss import BossSprite
import tmxloader
from item import get_items
from locals import Direction, MAPS_DIR

class Tile():
    def __init__(self, path, num):
        self.save_path = None
        self.map_path = None
        self.height = 0
        self.width = 0
        self.crates = []
        self.buttons = []
        self.gates = []
        self.bosses = []
        self.shooters = []
        self.enemies = []
        self.background = []
        self.foreground = []
        self.top = []

        if path and num:
            self.save_path = '{0}{1}'.format(path, num)
            self.map_path = '{0}{1}'.format(MAPS_DIR, num)
            tmxdata = tmxloader.load_pygame('{0}.tmx'.format(self.map_path), pixelalpha=True)
            self.height = tmxdata.height
            self.width = tmxdata.width
            data = json.loads(open('{0}.json'.format(self.save_path)).read())

            self._initialize_entities(data)
            self._initialize_map(tmxdata)

    def _initialize_entities(self, data):
        items = get_items() 
        for crate in data['crates']:
            self.crates.append(
                ObjectSprite(json=crate)
            )

        for button in data['buttons']:
            self.buttons.append(
                ButtonSprite(json=button)
            )

        for gate in data['gates']:
            self.gates.append(
                GateSprite(json=gate)
            )

        for boss in data['bosses']:
            self.bosses.append(
                BossSprite(json=boss)
            )

        for shooter in data['shooters']:
            self.shooters.append(
                ShooterSprite(json=shooter)
            )

        for enemy in data['enemies']:
            self.enemies.append(
                EnemySprite(json=enemy)
            )

    def _initialize_map(self, tmxdata):
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

    def save(self):
        with open('{0}.json'.format(self.save_path), 'w') as f:
            data = {'crates': [], 'shooters': [], 'enemies': [], 'buttons': [], 'bosses': [], 'gates': []}
            for crate in self.crates:
                data['crates'].append(crate.to_json())
            for shooter in self.shooters:
                data['shooters'].append(shooter.to_json())
            for enemy in self.enemies:
                data['enemies'].append(enemy.to_json())
            for button in self.buttons:
                data['buttons'].append(button.to_json())
            for boss in self.bosses:
                data['bosses'].append(boss.to_json())
            for gate in self.gates:
                data['gates'].append(gate.to_json())

            f.write(json.dumps(data))

    def is_walkable(self, x, y):
        try:
            if x < 0 or x > self.width or y < 0 or y > self.height:
                return True
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
