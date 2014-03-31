class ItemType:
    item = 0
    magicShoes = 1

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
    
