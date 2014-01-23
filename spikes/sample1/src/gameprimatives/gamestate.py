
class GameState:
    updatable = None
    renderable = None
    events = None
    screen = None
    res_path = "./"

    def __init__(self):
        self.updatable = []
        self.renderable = []
        self.events = []
        self.screen = None

    def resource(self, name):
        return self.res_path + name
