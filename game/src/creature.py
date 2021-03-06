import pygame
from entity import EntitySprite
from locals import Direction
from SpriteSheetAnim import SpriteStripAnim

class CreatureSprite(EntitySprite):
    def __init__(self, image_filename, position, size, direction):
        '''
        Initializes the CreatureSprite to be called from subclasses

        @param image_filename - The file name of spritesheet
        @param position - The position of the sprite on the map
        @param size - The size fo the sprite
        @param direction - The direction its facing in the game
        '''
        EntitySprite.__init__(self, position, size)
        self.action_wait_val = 12
        self.iters_until_action = 0
        self.direction = direction
        self._create_spritesheet(image_filename)

    def to_json(self):
        '''
        Serialize the import members of this class as a json object
        '''
        json = EntitySprite.to_json(self)
        json['action_wait_val'] = self.action_wait_val
        json['iters_until_action'] = self.iters_until_action
        json['direction'] = self.direction
        
        return json

    def from_json(self, json):
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''
        EntitySprite.from_json(self, json)
        self.action_wait_val = json['action_wait_val']
        self.iters_until_action = json['iters_until_action']
        self.direction = json['direction']
    
    def _create_spritesheet(self, image_filename):
        self.strips = self.imageStrips(image_filename)
        self.currentStrip = self.strips[self.direction]
        self.image = self._get_next_image()

    def _get_next_image(self):
        return pygame.Surface.convert_alpha(
            pygame.transform.scale(
                self.currentStrip.next(),
                (self.width, self.height)
            )
        )

    def imageStrips(self, image):
        '''
        Takes an spritesheet image file and turns them into strips to be animated in the game

        @param image - The spritesheet file
        '''
        strips = dict()
        strips[Direction.up] = SpriteStripAnim(image, (0,0,16,16), 4, (67,255,0), True, 4)
        strips[Direction.down] = SpriteStripAnim(image, (64,0,16,16), 4, (67,255,0), True, 4)
        strips[Direction.right] = SpriteStripAnim(image, (64, 17, 16, 16), 4, (67,255,0), True, 4)
        strips[Direction.left] = SpriteStripAnim(image, (0,17,16,16), 4, (67, 255, 0), True, 4)
        return strips

    def can_take_action(self):
        '''
        Boolean function to tell if the next action can be taken
        '''
        return self.iters_until_action <= 0

    def action_taken(self):
        '''
        Tells whether or not an action has been taken and updates 
        iters_until_action
        '''
        self.iters_until_action = self.action_wait_val

    def move(self, direction, tile):
        '''
        To be called when update. Moves the creature to the next tile

        @param direction - The direction to be moved in
        @param tile - The tile the creature is currently on
        '''

        (x, y) = self.coords
        if direction == Direction.up and tile.is_walkable(x, y - 1):
            y -= 1
            self.shiftby = (0,self.height)
        elif direction == Direction.down and tile.is_walkable(x, y + 1):
            y += 1
            self.shiftby = (0,-self.height)
        elif direction == Direction.left and tile.is_walkable(x - 1, y):
            x -= 1
            self.shiftby = (self.width, 0)
        elif direction == Direction.right and tile.is_walkable(x + 1, y):
            x += 1
            self.shiftby = (-self.width, 0)
        self.coords = (x, y)

    def isOutOfBounds(self, width, height, left, right, up, down):
        '''
        Tells whether or not the sprite is out of bounds

        @param width - The width of the sprite
        @param height - The height of the sprite
        @param left - coordinate of left side of game world
        @param right - coordinate of right side of game world
        @param down - coordinate of bottom of game world
        @param up - coordinate of bootom of game world
        '''

        (x, y) = self.coords
        (px, py) = (x, y)
        
        if x < 0:
            x = 0
            (px, py) = (left, y)
        elif x > width - 1: 
            x = width - 1
            (px, py) =  (right, y)
        elif y < 0: 
            y = 0
            (px, py) =  (x, up)
        elif y > height - 1: 
            y = height - 1
            (px, py) =  (x, down)

        self.coords = (x, y)
        if (px, py) != (x, y):
            self.handleOutOfBounds(px, py, left, right, up, down)
        return (px, py)

    # Callback function for being out of bounds
    def handleOutOfBounds(self, px, py, left, right, up, down):
        '''
        To be implemented in subclasses

        @param px - x coordinate
        @param py - y coordinate
        @param left - coordinate of left side of game world
        @param right - coordinate of right side of game world
        @param down - coordinate of bottom of game world
        @param up - coordinate of bootom of game world
        '''
        pass

    def update (self):
        '''
        The update function changes the sprite to look like its moving
        and calls the entity update function
        '''
        if self.currentStrip is self.strips[self.direction]:
            self.image = self._get_next_image()
        else:
            self.currentStrip = self.strips[self.direction]
            self.image = self._get_next_image()
        self.currentStrip = self.strips[self.direction]
        EntitySprite.update(self)
        
