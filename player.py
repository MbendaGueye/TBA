# Define the Player class.
class Player:
    """
    This class represents the player in the game.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The room where the player is currently located.

    Methods:
        __init__(self, name):
            Initializes the Player instance with a name and sets the current room to None.
        move(self, direction):
            Moves the player to the room in the specified direction if possible.

    Example:
        >>> player = Player("Alex")
        >>> player.name
        'Alex'
        >>> player.current_room = Room("Forest", "a lush forest.")
        >>> player.current_room.name
        'Forest'
    """


    DIRECTIONS = {
        "N": "N", "NORD": "N",
        "E": "E", "EST": "E",
        "S": "S", "SUD": "S",
        "O": "O", "OUEST": "O",
        "U": "U", "UP": "U",
        "D": "D", "DOWN": "D"
    }

    def __init__(self, name):
        self.name = name
        self.current_room = None

    def move(self, direction):
        normalized_direction = self.DIRECTIONS.get(direction.upper())
        if not normalized_direction:
            print(f"\n'{direction}' n'est pas une direction valide.\n")
            return False
        next_room = self.current_room.exits.get(normalized_direction)
        if not next_room:
            print("\nAucune porte dans cette direction !\n")
            return False
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
