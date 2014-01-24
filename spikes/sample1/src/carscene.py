from gameprimatives.gamescene import *
from car import *
from menuscene import *

class CarScene(GameScene):

    def __init__(self, game_state):
        self.gameobjs = [Car(game_state)]

    def update(self, game_state):
        for event in game_state.events:
            if not hasattr(event, 'key') or event.type != KEYDOWN: continue
            if event.key == K_p: self.gameobjs.insert(0, Car(game_state))
            elif event.key == K_q: 
                game_state.push_scene(MenuScene(["One", "Two", "Three"]))
                

        super(CarScene, self).update(game_state)

    def should_update(self, game_state):
        return game_state.top_scene() == self

    def should_render(self, game_state):
        return True
