class ItemType:
    item = 0
    magicShoes = 1

class Item:
    name = 'Item'
    type = ItemType.item
    
    @staticmethod
    def use():
	print 'Used Item'
        
class MagicShoes(Item):
    name = 'Magic Shoes'
    type = ItemType.magicShoes

    @staticmethod
    def use():
        print 'Used Magic Shoes'
    
