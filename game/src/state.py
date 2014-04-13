class State:
    screen = None
    screens = []

    @staticmethod
    def push_screen(new_screen):
        State.screens.insert(0, new_screen)

    @staticmethod
    def pop_screen():
        State.screens.pop(0)
	
