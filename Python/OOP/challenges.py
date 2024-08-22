class CodeWarrior():
    """A programming hero class for an as-yet unfinished pixel-art game. This
    class is intended to represent player-characters in the game's state.
    
    Class Attributes:
        - base_health: an integer equal to 100
        - inventory_size: an integer equal to 5
    
    Instance Attributes (created by the __init__ method, but listed here for convenience):
        - self.character_name: A string to store the character's name
        - self.current_health: An integer representing the character's current health
        - self.inventory_list: A list to store any items the player picks up
    """

    # don't forget to define your class attributes!

    def __init__(self, character_name: str):
        """The init method, which creates instances of this class. 
        
        Arguments:
            - character_name: a string representing the name of the created character

        Actions:
            - sets the value of self.inventory_list to an empty list
            - sets the value of self.current_health to the value of the class's base_health 
            - sets the value of self.character_name to the value supplied
        
        Returns: an __init__ function should not include a Return statement!
        """
        pass

    def pick_up_item(self, item_name: str):
        """Appends an item to the player's inventory. Max number of inventory 
        items is the class's inventory_size amount.
        
        Arguments: 
            - item_name: a string representing the name of the item the player
            picked up

        Returns: no return necessary
        """
        pass

    def update_health(self, health_change: int):
        """Modifies the player's health. Minimum value is 0, maximum value is 
        the class's base_health value.
        
        Arguments: 
            - health_change: an integer representing the change to the health amount

        Returns: no return necessary
        """
        pass
