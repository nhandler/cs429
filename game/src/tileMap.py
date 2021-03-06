import json
from locals import MAPS_DIR
from tile import Tile

class TileMap():
    height = 12
    width = 12
    BLOCK_SIZE = (60, 60)
    TILE_UP = -1
    TILE_DOWN = -2
    TILE_LEFT = -1
    TILE_RIGHT = -2

    def __init__(self, filename):
        self.x = 0
        self.y = 0
        self.save_path = filename
        self.load()
        mapdata = json.loads(open(MAPS_DIR + 'main_map.json').read())
        self.tilemapping = map(None, *mapdata["map"])
        self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y])

    def save(self, player):
        self.tile.save()
        player.save(self.save_path)
        with open('{0}current_tile.json'.format(self.save_path), 'w') as f:
            f.write(json.dumps(self.to_json()))

    def load(self):
        with open('{0}current_tile.json'.format(self.save_path), 'r') as f:
            data = json.loads(f.read())
            self.x = data['x']
            self.y = data['y']

    def to_json(self):
        json = {'x': self.x, 'y': self.y}
        return json

    def set_tile(self, player, x, y):
        self.x = x
        self.y = y
        self.save(player)
        self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y], TileMap.BLOCK_SIZE)


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

        if (px == TileMap.TILE_LEFT and self.x - 1 >= 0 and self.tilemapping[self.x-1][self.y]):
            self.x -= 1
            self.save(player)
            self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y])
            player.coords = (self.width-1, py)
            return False
        elif (px == TileMap.TILE_RIGHT and self.x + 1 < len(self.tilemapping) and self.tilemapping[self.x+1][self.y]):
            self.x += 1
            self.save(player)
            self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y])
            player.coords = (0, py)
            return False
        
        if (py == TileMap.TILE_UP and self.y - 1 >= 0 and self.tilemapping[self.x][self.y-1]):
            self.y -= 1
            self.save(player)
            self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y])
            player.coords = (px, self.height-1)
            return False
        elif (py == TileMap.TILE_DOWN and self.y + 1 < len(self.tilemapping[self.x]) and self.tilemapping[self.x][self.y+1]):
            self.y += 1
            self.save(player)
            self.tile = Tile(self.save_path, self.tilemapping[self.x][self.y])
            player.coords = (px, 0)
            return False
        
        return True

    def draw(self, surface):
        self.tile.draw_background(surface)
        self.tile.draw_foreground(surface)
        self.tile.draw_top(surface)
