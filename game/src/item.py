<<<<<<< HEAD
class Item:
    name = 'Item'
=======
from state import State

class Item:
    def __init__(self):
        self.name = 'Item'
>>>>>>> Removing item integer types
    
    @staticmethod
    def use(player):
	print 'Used Item'
        
class MagicShoes(Item):
<<<<<<< HEAD
    name = 'Magic Shoes'
=======
    def __init__(self):
        self.name = 'Magic Shoes'
>>>>>>> Removing item integer types

    @staticmethod
    def use(player):
        print 'Used Magic Shoes'
    
    
class Potion(Item):
<<<<<<< HEAD
    name = 'Potion'
=======
    def __init__(self):
        self.name = 'Potion'
>>>>>>> Removing item integer types

    @staticmethod
    def use(player):
        player.health += 10

class Crystal(Item):
<<<<<<< HEAD
    name = 'Energy Crystal'
    
    @staticmethod
    def use(player):
        player.laser += 1

class FinalItem1(Item):
    name = 'Goat\'s Foot'
=======
    def __init__(self):
        self.name = 'Energy Crystal'
        
    def use(self):
        State.player.laser += 1

class FinalItem1(Item):
    def __init__(self):
        self.name = 'Goat\'s Foot'
>>>>>>> Removing item integer types

    @staticmethod
    def use(player):
        pass

class FinalItem2(Item):
<<<<<<< HEAD
    name = 'Virgin Sacrifice'
=======
    def __init__(self):
        self.name = 'Virgin Sacrifice'
>>>>>>> Removing item integer types

    def use(player):
        pass

class FinalItem3(Item):
<<<<<<< HEAD
    name = 'Ghost Soul'
=======
    def __init__(self):
        self.name = 'Ghost Soul'
>>>>>>> Removing item integer types
        
    def use(player):
        pass

class FinalItem4(Item):
<<<<<<< HEAD
    name = 'Narcissus'
=======
    def __init__(self):
        self.name = 'Narcissus'
>>>>>>> Removing item integer types
        
    def use(player):
        pass

class ItemType:
    final_items = [FinalItem1, FinalItem2, FinalItem3, FinalItem4 ]
<<<<<<< HEAD
=======

>>>>>>> Removing item integer types
