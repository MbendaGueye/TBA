class Character:
    """
    Represents a non-player character (NPC) in the game.

    Attributes:
        name (str): The name of the character.
        description (str): A description of the character.
        current_room (Room): The room where the character is located.
        messages (list[str]): Messages the character says when interacted with.
        synonyms (list[str]): Synonyms or alternative names for the character.
    """

    def __init__(self, name: str, description: str, current_room: "Room", messages: list[str] = None, synonyms: list[str] = None):
        """
        Initializes a Character instance.

        Args:
            name (str): The name of the character.
            description (str): A description of the character.
            current_room (Room): The room where the character is located.
            messages (list[str], optional): The messages the character says. Defaults to None.
            synonyms (list[str], optional): Synonyms for the character's name. Defaults to None.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.messages = messages or []
        self.synonyms = synonyms or []

    def talk(self, game: "Game") -> str:
        """
        Defines the behavior when interacting with the character.

        For specific characters like "Monstre BOUBOU", this method implements custom logic.

        Args:
            game (Game): The current game instance.

        Returns:
            str: The message the character says.
        """
        player = game.player

        if self.name.lower() == "monstre boubou":
            # Custom logic for the monster
            if not player.inventory.get_item_by_name("sword"):
                game.finished = True
                return "Le monstre vous a attaqué et tué ! VOUS AVEZ PERDU."
            return "Bats-toi si tu es courageux ! Je vais t'écraser."

        if self.messages:
            return self.messages.pop(0)
        return "..."

    def matches_name(self, input_name: str) -> bool:
        """
        Checks if the input name matches the character's name or its synonyms.

        Args:
            input_name (str): The name to check.

        Returns:
            bool: True if it matches, False otherwise.
        """
        input_name = input_name.lower()
        return input_name == self.name.lower() or input_name in (syn.lower() for syn in self.synonyms)

    def __str__(self) -> str:
        """
        Returns a string representation of the character.

        Returns:
            str: The name and description of the character.
        """
        return f"{self.name} : {self.description}"
