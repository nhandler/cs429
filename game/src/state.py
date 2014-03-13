class State:
    screens = None
    health = 3

    @staticmethod
    def push_screen(screen):
        State.screens.insert(0, screen)

    @staticmethod
    def pop_screen():
        State.screens.pop(0)