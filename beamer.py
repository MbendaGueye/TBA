"""
Module contenant la classe Beamer, un objet magique permettant la téléportation.

La classe Beamer hérite de la classe Item et ajoute des fonctionnalités
spécifiques pour charger une pièce et permettre la téléportation.
"""

from item import Item
from room import Room


class Beamer(Item):
    """
    Un objet magique qui permet la téléportation vers une pièce visitée précédemment.

    Attributs:
        charged_room (Room | None): La pièce où le Beamer est chargé.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Initialise une instance de Beamer.

        Args:
            name (str): Le nom du Beamer.
            description (str): Une description du Beamer.
            weight (float): Le poids du Beamer.
        """
        super().__init__(name, description, weight)
        self.charged_room: Room | None = None

    def charge(self, room: Room) -> None:
        """
        Charge le Beamer avec une pièce spécifique.

        Args:
            room (Room): La pièce à associer au Beamer.
        """
        self.charged_room = room
        print(f"\nLe Beamer '{self.name}' est chargé avec la pièce '{room.name}'.\n")
