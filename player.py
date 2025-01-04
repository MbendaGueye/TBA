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

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True
