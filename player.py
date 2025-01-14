"""
Module contenant la classe Player, représentant le joueur dans le jeu.
"""

from base_character import BaseCharacter
from inventory import Inventory
from room import Room
from item import Item
from beamer import Beamer


class Player(BaseCharacter):
    """
    Représente le joueur dans le jeu.

    Attributs:
        inventory (Inventory): L'inventaire du joueur.
        max_weight (float): Le poids maximum que le joueur peut transporter.
        history (list[Room]): L'historique des pièces visitées par le joueur.
    """

    DIRECTIONS = {
        "N": "N", "NORD": "N",
        "E": "E", "EST": "E",
        "S": "S", "SUD": "S",
        "O": "O", "OUEST": "O",
        "U": "U", "UP": "U",
        "D": "D", "DOWN": "D"
    }

    def __init__(self, name: str, max_weight: float = 10.0):
        """
        Initialise une instance de Player.

        Args:
            name (str): Le nom du joueur.
            max_weight (float): Le poids maximum que le joueur peut transporter.
        """
        super().__init__(name, "Un aventurier courageux.")
        self.inventory = Inventory()
        self.max_weight = max_weight
        self.history: list[Room] = []

    def move(self, direction: str) -> bool:
        """
        Déplace le joueur vers une nouvelle pièce si possible.

        Args:
            direction (str): La direction du déplacement.

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        """
        normalized_direction = self.DIRECTIONS.get(direction.upper())
        if not normalized_direction:
            print(f"\n'{direction}' n'est pas une direction valide.\n")
            return False

        next_room = self.current_room.exits.get(normalized_direction)
        if not next_room:
            print("\nAucune porte dans cette direction !\n")
            return False

        if next_room.door and next_room.door.is_locked():
            print("\nLa porte vers cette pièce est verrouillée.\n")
            return False

        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def use_beamer(self) -> bool:
        """
        Utilise un Beamer pour téléporter le joueur à la pièce précédente.

        Returns:
            bool: True si la téléportation a réussi, False sinon.
        """
        beamer = next(
            (item for item in self.inventory.items if isinstance(item, Beamer)),
            None
        )
        if not beamer:
            print("\nVous n'avez pas de Beamer dans votre inventaire.\n")
            return False

        if not self.history:
            print("\nAucune pièce précédente pour utiliser le Beamer.\n")
            return False

        self.current_room = self.history.pop()
        print(f"\nVous avez été téléporté à : {self.current_room.name}\n")
        return True

    def get_history(self) -> str:
        """
        Retourne l'historique des déplacements du joueur.

        Returns:
            str: Une chaîne formatée des déplacements du joueur.
        """
        if not self.history:
            return "\nAucun lieu visité pour l'instant.\n"
        history_descriptions = [
            f"- {room.description}" for room in self.history
        ]
        return (
            "\nVous avez déjà visité les pièces suivantes :\n" +
            "\n".join(history_descriptions) + "\n"
        )

    def get_total_weight(self) -> float:
        """
        Retourne le poids total des objets dans l'inventaire du joueur.

        Returns:
            float: Le poids total des objets.
        """
        return sum(item.weight for item in self.inventory.items)

    def can_take_item(self, item: Item) -> bool:
        """
        Vérifie si le joueur peut prendre un objet sans dépasser le poids maximal.

        Args:
            item (Item): L'objet à vérifier.

        Returns:
            bool: True si l'objet peut être pris, False sinon.
        """
        return self.get_total_weight() + item.weight <= self.max_weight

    def add_item(self, item: Item) -> None:
        """
        Ajoute un objet à l'inventaire du joueur.

        Args:
            item (Item): L'objet à ajouter.
        """
        self.inventory.add_item(item)
        print(f"\n{item.name} a été ajouté à votre inventaire.\n")

    def remove_item(self, item: Item) -> None:
        """
        Retire un objet de l'inventaire du joueur.

        Args:
            item (Item): L'objet à retirer.
        """
        self.inventory.remove_item(item)
        print(f"\n{item.name} a été retiré de votre inventaire.\n")

    def get_inventory(self) -> str:
        """
        Retourne l'inventaire du joueur sous forme de chaîne.

        Returns:
            str: Une représentation textuelle de l'inventaire.
        """
        return self.inventory.get_inventory()

    def is_inventory_empty(self) -> bool:
        """
        Vérifie si l'inventaire du joueur est vide.

        Returns:
            bool: True si l'inventaire est vide, False sinon.
        """
        return self.inventory.is_empty()
