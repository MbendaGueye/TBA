"""
Module contenant la classe Room pour représenter les pièces du jeu.
"""
from inventory import Inventory
from door import Door
from character import Character


class Room:
    """
    Représente une pièce dans le jeu.
    """

    VALID_DIRECTIONS = {"N", "E", "S", "O", "U", "D"}

    def __init__(self, name: str, description: str, dark: bool = False):
        """
        Initialise une pièce.

        Args:
            name (str): Le nom de la pièce.
            description (str): Une description de la pièce.
            dark (bool): Indique si la pièce est sombre. Par défaut, False.
        """
        self.name: str = name
        self.description: str = description
        self.exits: dict[str, "Room"] = {}
        self.inventory = Inventory()
        self.dark = dark
        self.door: Door | None = None  # Porte optionnelle pour restreindre l'accès
        self.characters: list[Character] = []  # Liste des personnages dans la pièce

    def is_dark(self) -> bool:
        """
        Vérifie si la pièce est sombre.

        Returns:
            bool: True si la pièce est sombre, False sinon.
        """
        return self.dark

    def get_exit_string(self) -> str:
        """
        Retourne une chaîne décrivant les sorties disponibles.

        Returns:
            str: Une chaîne formatée listant les sorties.
        """
        return "Sorties: " + ", ".join(self.exits.keys())

    def get_long_description(self) -> str:
        """
        Retourne une description détaillée de la pièce, incluant les sorties,
        l'inventaire et les personnages.

        Returns:
            str: Une description détaillée de la pièce.
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
        Affiche la description de la pièce et de son contenu.
        """
        print(self.get_long_description())
