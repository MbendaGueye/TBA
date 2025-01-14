"""
Module contenant la classe BaseCharacter, qui sert de classe de base pour les personnages du jeu.

Cette classe peut être utilisée pour représenter à la fois les joueurs et les personnages
non joueurs (PNJ) dans le jeu.
"""

class BaseCharacter:
    """
    Représente un personnage de base dans le jeu (joueur ou personnage non joueur).

    Attributs:
        name (str): Le nom du personnage.
        description (str): Une brève description du personnage.
        current_room (Room | None): La pièce où se trouve actuellement le personnage.
    """

    def __init__(self, name: str, description: str = ""):
        """
        Initialise une instance de BaseCharacter.

        Args:
            name (str): Le nom du personnage.
            description (str, facultatif): Une brève description du personnage. Par défaut, une chaîne vide.
        """
        self.name = name
        self.description = description
        self.current_room = None

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne du personnage.

        Returns:
            str: Le nom et la description du personnage.
        """
        return f"{self.name} : {self.description}"
