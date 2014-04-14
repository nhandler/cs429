def get_items():
    return {
        'None': None,
        'Magic Shoes': MagicShoes,
        'potion': Potion,
        'crystal': Crystal,
        'Goat\'s Foot': FinalItem1,
        'Virgin Sacrifice': FinalItem2,
        'Ghost Soul': FinalItem3,
        'Narcissus': FinalItem4,
    }

class Item:
    name = 'Item'
    
    @staticmethod
    def use(player):
	print 'Used Item'
        
class MagicShoes(Item):
    name = 'Magic Shoes'

    @staticmethod
    def use(player):
        print 'Used Magic Shoes'
    
    
class Potion(Item):
    name = 'Potion'

    @staticmethod
    def use(player):
        player.health += 10

class Crystal(Item):
    name = 'Energy Crystal'
    
    @staticmethod
    def use(player):
        player.laser += 1

class FinalItem1(Item):
    name = 'Goat\'s Foot'

    @staticmethod
    def use(player):
        pass

class FinalItem2(Item):
    name = 'Virgin Sacrifice'

    def use(player):
        pass

class FinalItem3(Item):
    name = 'Ghost Soul'
        
    def use(player):
        pass

class FinalItem4(Item):
    name = 'Narcissus'
        
    def use(player):
        pass

class ItemType:
    final_items = [FinalItem1, FinalItem2, FinalItem3, FinalItem4 ]
