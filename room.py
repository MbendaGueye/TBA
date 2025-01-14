from inventory import Inventory
from door import Door
from character import Character


class Room:
    """
    Represents a room in the game.
    """

    VALID_DIRECTIONS = {"N", "E", "S", "O", "U", "D"}

    def __init__(self, name: str, description: str, dark=False):
        """
        Initializes the room.

        Args:
            name (str): The name of the room.
            description (str): A description of the room.
            dark (bool): Indicates if the room is dark. Default is False.
        """
        self.name: str = name
        self.description: str = description
        self.exits: dict[str, "Room"] = {}
        self.inventory = Inventory()
        self.dark = dark
        self.door: Door | None = None  # Optional door to restrict access
        self.characters: list[Character] = []  # List of characters in the room

    def is_dark(self) -> bool:
        """
        Checks if the room is dark.

        Returns:
            bool: True if the room is dark, False otherwise.
        """
        return self.dark

    def get_exit_string(self) -> str:
        """
        Returns a string describing the exits available in the room.

        Returns:
            str: A formatted string listing the exits.
        """
        return "Sorties: " + ", ".join(self.exits.keys())

    def get_long_description(self) -> str:
        """
        Returns a detailed description of the room, including exits, inventory, and characters.

        Returns:
            str: A detailed description of the room.
        """
        if self.door and self.door.is_locked():
            return "La porte vers cette pièce est verrouillée.\n"

        description = f"\nVous êtes dans {self.description}\n"
        description += f"{self.inventory.get_inventory()}\n"
        if self.characters:
            characters_desc = "\n".join([f"- {char}" for char in self.characters])
            description += f"Personnages présents :\n{characters_desc}\n"
        description += f"{self.get_exit_string()}\n"
        return description

    def look(self) -> None:
        """
        Displays the description of the room and its contents.
        """
        print(self.get_long_description())

    def find_character_by_name(self, name: str) -> Character | None:
        """
        Finds a character in the room by their name or synonyms.

        Args:
            name (str): The name or synonym of the character.

        Returns:
            Character | None: The character if found, None otherwise.
        """
