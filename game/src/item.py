from state import State

class Item:
    def __init__(self):
        self.name = 'Item'
    
    def use(self):
	print 'Used Item'
        
class MagicShoes(Item):
    def __init__(self):
        self.name = 'Magic Shoes'

    def use(self):
        print 'Used Magic Shoes'
    
    
class Potion(Item):
    def __init__(self):
        self.name = 'Potion'

    def use(self):
        State.player.health += 10

class Crystal(Item):
    def __init__(self):
        self.name = 'Energy Crystal'
        
    def use(self):
        State.player.laser += 1

class FinalItem1(Item):
    def __init__(self):
        self.name = 'Goat\'s Foot'

    def use(self):
        pass

class FinalItem2(Item):
    def __init__(self):
        self.name = 'Virgin Sacrifice'

    def use(self):
        pass

class FinalItem3(Item):
    def __init__(self):
        self.name = 'Ghost Soul'
        
    def use(self):
        pass

class FinalItem4(Item):
    def __init__(self):
        self.name = 'Narcissus'
        
    def use(self):
        pass

class ItemType:
    final_items = [FinalItem1, FinalItem2, FinalItem3, FinalItem4 ]

