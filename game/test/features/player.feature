Feature: Player Item Inventory
    An item should be able to be
    added to a player's inventory.

    Scenario: Add Item
        Given The player is at (60, 60)
        When I add an item to its inventory
        Then The item is in the inventory
