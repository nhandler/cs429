
class GameState:
    gameobjs = None
    events = None
    screen = None
    res_path = "./"
    is_running = True

    def __init__(self):
        self.gameobjs = []
        self.events = []
        self.screen = None
        self.is_running = True

    def resource(self, name):
        return self.res_path + name

    def push_scene(self, scene):
        self.gameobjs.insert(0, scene)

    def pop_scene(self):
        self.gameobjs.pop(0)

    def top_scene(self):
        return self.gameobjs[0]
