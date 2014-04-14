from state import State

class ItemType:
    item = 0
    magicShoes = 1
    potion = 2
    crystal = 3
    final1 = 4
    final2 = 5
    final3 = 6 
    final4 = 7
    final_items = [ 4, 5, 6, 7 ]

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

class FinalItem1(Item):
    def __init__(self):
        self.name = 'Goat\'s Foot'
        self.type = ItemType.final1

    def use(self):
        pass

class FinalItem2(Item):
    def __init__(self):
        self.name = 'Virgin Sacrifice'
        self.type = ItemType.final2

    def use(self):
        pass

class FinalItem3(Item):
    def __init__(self):
        self.name = 'Ghost Soul'
        self.type = ItemType.final3
        
    def use(self):
        pass

class FinalItem4(Item):
    def __init__(self):
        self.name = 'Narcissus'
        self.type = ItemType.final4
        
    def use(self):
        pass
