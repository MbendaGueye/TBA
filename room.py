# Define the Room class.

class Room:
    """
    This class represents a room in the game.

    Attributes:
        name (str): The name of the room.
        description (str): A detailed description of the room.
        exits (dict): A dictionary mapping cardinal directions (N, E, S, O) to connected rooms.

    Methods:
        __init__(self, name, description):
            Initializes the Room instance with a name, description, and an empty exits dictionary.
        get_exit(self, direction):
            Returns the room in the given direction if it exists, otherwise None.
        get_exit_string(self):
            Returns a string describing the exits available in the room.
        get_long_description(self):
            Returns a long description of the room, including exits.

    Example:
        >>> room = Room("Forest", "a lush green forest with tall trees.")
        >>> room.name
        'Forest'
        >>> room.description
        'a lush green forest with tall trees.'
        >>> room.get_exit("N")
        None
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
