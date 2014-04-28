import os
import shutil
from locals import CURRENT_GAME_DIR

def save(save_dir):
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    shutil.copytree(CURRENT_GAME_DIR, save_dir)

def load(save_dir):
    if os.path.exists(CURRENT_GAME_DIR):
        shutil.rmtree(CURRENT_GAME_DIR)
    try:
        shutil.copytree(save_dir, CURRENT_GAME_DIR)
    except OSError:
        print 'Save not found!'

class State:
    boss_ready = False
    screen = None
    screens = []
    save_name = ''

    @staticmethod
    def push_screen(new_screen):
        State.screens.insert(0, new_screen)

    @staticmethod
    def pop_screen():
        State.screens.pop(0)
