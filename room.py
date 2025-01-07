class Room:
    """
    Represents a room in the game.
    """

    VALID_DIRECTIONS = {"N", "E", "S", "O", "U", "D"}

    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description
        self.exits: dict[str, "Room"] = {}

    def get_exit_string(self) -> str:
        """
        Returns a string describing the exits available in the room.
        """
        return "Sorties: " + ", ".join(self.exits.keys())

    def get_long_description(self) -> str:
        """
        Returns a long description of the room, including exits.
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
