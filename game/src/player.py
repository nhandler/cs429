from creature import CreatureSprite

class PlayerSprite (CreatureSprite):
    def __init__(self, image, position):
        CreatureSprite.__init__(self, image, position)
