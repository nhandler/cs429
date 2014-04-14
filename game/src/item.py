class ItemType:
    item = 0
    magicShoes = 1
    potion = 2
    crystal = 3

class Item:
    name = 'Item'
    type = ItemType.item
    
    @staticmethod
    def use(player):
	print 'Used Item'
        
class MagicShoes(Item):
    name = 'Magic Shoes'
    type = ItemType.magicShoes

    @staticmethod
    def use(player):
        print 'Used Magic Shoes'
    
    
class Potion(Item):
    name = 'Potion'
    type = ItemType.potion;

    @staticmethod
    def use(player):
        player.health += 10

class Crystal(Item):
    name = 'Energy Crystal'
    type = ItemType.crystal;
    
    @staticmethod
    def use(player):
        player.laser += 1
