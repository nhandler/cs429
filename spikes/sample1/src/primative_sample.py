import pygame, math, sys

import cProfile
from pygame.locals import *

from gameprimatives.game import *
from gameprimatives.gamestate import GameState
from carscene import CarScene
#import gameprimatives.game, gameprimatives.gamestate, gameprimatives.carscene



game = Game((1024,768))
game_state = GameState()
game_state.res_path = "../res/"
carscene = CarScene(game_state)
game_state.renderable = [carscene]
game_state.updatable = [carscene]

cProfile.run('game.launch(game_state)')
#game.launch(game_state)
