from inventory import Inventory
from door import Door


class Room:
    """
    Represents a room in the game.
    """

    VALID_DIRECTIONS = {"N", "E", "S", "O", "U", "D"}

    def __init__(self, name: str, description: str, dark=False):
        self.name: str = name
        self.description: str = description
        self.exits: dict[str, "Room"] = {}
        self.inventory = Inventory()
        self.dark = dark
        self.door: Door | None = None  # Optional door to restrict access

    def is_dark(self) -> bool:
        """Checks if the room is dark."""
        return self.dark

    def get_exit_string(self) -> str:
        """
        Returns a string describing the exits available in the room.
        """
        return "Sorties: " + ", ".join(self.exits.keys())

    def get_long_description(self) -> str:
        """
        Returns a detailed description of the room, including exits and inventory.

        Returns:
            str: A detailed description of the room.
        """
        if self.door and self.door.is_locked():
            return "La porte vers cette pièce est verrouillée.\n"

        # Si la porte est déverrouillée, affiche la description complète
        description = f"\nVous êtes dans {self.description}\n"
        description += f"\n{self.inventory.get_inventory()}\n{self.get_exit_string()}\n"
        return description
    
    def look(self) -> None:
        """
        Displays the description of the room and the items present.
        """
        print(self.get_long_description())
