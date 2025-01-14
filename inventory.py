"""
Module contenant la classe Inventory, qui représente un inventaire pour stocker des objets dans le jeu.
"""

from item import Item


class Inventory:
    """
    Représente un inventaire pouvant contenir des objets.

    Attributs:
        items (set): Un ensemble contenant les objets présents dans l'inventaire.
    """

    def __init__(self):
        """
        Initialise un inventaire vide.
        """
        self.items = set()

    def add_item(self, item: Item) -> None:
        """
        Ajoute un objet à l'inventaire.

        Args:
            item (Item): L'objet à ajouter.
        """
        self.items.add(item)

    def remove_item(self, item: Item) -> None:
        """
        Retire un objet de l'inventaire.

        Args:
            item (Item): L'objet à retirer.
        """
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item.name} n'est pas dans l'inventaire.")

    def get_inventory(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de l'inventaire.

        Returns:
            str: Une chaîne formatée listant les objets dans l'inventaire.
        """
        if not self.items:
            return "L'inventaire est vide."

        inventory_details = [
            f"- {item.name} : {item.description} ({item.weight} kg)"
            for item in self.items
        ]
        return "Contenu de l'inventaire :\n" + "\n".join(inventory_details)

    def is_empty(self) -> bool:
        """
        Vérifie si l'inventaire est vide.

        Returns:
            bool: True si l'inventaire est vide, False sinon.
        """
        return len(self.items) == 0

    def get_item_by_name(self, name: str) -> Item | None:
        """
        Trouve un objet dans l'inventaire en fonction de son nom.

        Args:
            name (str): Le nom de l'objet à chercher.

        Returns:
            Item | None: L'objet correspondant si trouvé, None sinon.
        """
        for item in self.items:
            if item.name == name:
                return item
        return None
