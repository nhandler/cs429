class State:
    screens = None
    inventory = None
    player = None
    screen = None
    boss_ready = False

    @staticmethod
    def push_screen(screen):
        State.screens.insert(0, screen)

    @staticmethod
    def pop_screen():
        State.screens.pop(0)
	
