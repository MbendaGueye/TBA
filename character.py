"""
Module contenant la classe Character, représentant un personnage non-joueur (NPC) dans le jeu.
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from room import Room
    from game import Game


class Character:
    """
    Représente un personnage non-joueur (NPC) dans le jeu.

    Attributes:
        name (str): Le nom du personnage.
        description (str): Une description du personnage.
        current_room (Room): La pièce où se trouve le personnage.
        messages (List[str]): Messages que le personnage dit lorsqu'il est interagi.
        synonyms (List[str]): Synonymes ou noms alternatifs pour le personnage.
    """

    def __init__(
        self,
        name: str,
        description: str,
        current_room: "Room",
        messages: List[str] = None,
        synonyms: List[str] = None
    ):
        """
        Initialise une instance de Character.

        Args:
            name (str): Le nom du personnage.
            description (str): Une description du personnage.
            current_room (Room): La pièce où se trouve le personnage.
            messages (List[str], optional): Les messages que le personnage dit. Par défaut, None.
            synonyms (List[str], optional): Synonymes pour le nom du personnage. Par défaut, None.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.messages = messages or []
        self.synonyms = synonyms or []

    def talk(self, game: "Game") -> str:
        """
        Définit le comportement lors de l'interaction avec le personnage.

        Implémente une logique spécifique pour des personnages comme "Monstre BOUBOU".

        Args:
            game (Game): L'instance actuelle du jeu.

        Returns:
            str: Le message que dit le personnage.
        """
        player = game.player

        if self.name.lower() == "monstre boubou":
            # Logique personnalisée pour le monstre
            if not player.inventory.get_item_by_name("sword"):
                game.finished = True
                return "Le monstre vous a attaqué et tué ! VOUS AVEZ PERDU."
            return "Bats-toi si tu es courageux ! Je vais t'écraser."

        if self.messages:
            return self.messages.pop(0)
        return "..."

    def matches_name(self, input_name: str) -> bool:
        """
        Vérifie si le nom donné correspond au nom du personnage ou à ses synonymes.

        Args:
            input_name (str): Le nom à vérifier.

        Returns:
            bool: True si le nom correspond, sinon False.
        """
        input_name = input_name.lower()
        return input_name == self.name.lower() or input_name in (
            syn.lower() for syn in self.synonyms
        )

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du personnage.

        Returns:
            str: Le nom et la description du personnage.
        """
        return f"{self.name} : {self.description}"
