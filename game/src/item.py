from state import State

class ItemType:
    item = 0
    magicShoes = 1
    potion = 2
    crystal = 3

class Item:
    def __init__(self):
        self.name = 'Item'
        self.type = ItemType.item
    
    def use(self):
	print 'Used Item'
        
class MagicShoes(Item):
    def __init__(self):
        self.name = 'Magic Shoes'
        self.type = ItemType.magicShoes

    def use(self):
        print 'Used Magic Shoes'
    
    
class Potion(Item):
    def __init__(self):
        self.name = 'Potion'
        self.type = ItemType.potion;

    def use(self):
        State.player.health += 10

class Crystal(Item):
    def __init__(self):
        self.name = 'Energy Crystal'
        self.type = ItemType.crystal;
        
    def use(self):
        State.player.laser += 1
