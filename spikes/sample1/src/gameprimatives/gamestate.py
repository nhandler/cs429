
class GameState:
    gameobjs = None
    events = None
    screen = None
    res_path = "./"

    def __init__(self):
        self.gameobjs = []
        self.events = []
        self.screen = None

    def resource(self, name):
        return self.res_path + name

    def push_scene(self, scene):
        self.gameobjs.insert(0, scene)

    def pop_scene(self):
        self.gameobjs.pop(0)

    def top_scene(self):
        print self.gameobjs
        return self.gameobjs[0]
