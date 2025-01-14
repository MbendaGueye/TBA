class BaseCharacter:
    """
    Represents a base character in the game (either a player or a non-player character).

    Attributes:
        name (str): The name of the character.
        description (str): A brief description of the character.
        current_room (Room | None): The room where the character is located.
    """

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.current_room = None

    def __str__(self) -> str:
        """
        Returns a string representation of the character.

        Returns:
            str: The character's name and description.
        """
        return f"{self.name} : {self.description}"
