from creature import CreatureSprite, HorizontalMovement, VerticalMovement, Direction

class PlayerSprite (CreatureSprite):
    def __init__(self, image, position):
        CreatureSprite.__init__(self, image, position)
