from gameobject import *

class GameScene(GameObject):
    gameobjs = None

    def __init__(self):
        gameobjs = []

    def update(self, game_state):
        for obj in self.gameobjs:
            if obj.should_update(game_state):
                obj.update(game_state)

    def render(self, game_state):
        for obj in self.gameobjs:
            if obj.should_render(game_state):
                obj.render(game_state)
        
