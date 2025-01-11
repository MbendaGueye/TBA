from item import Item


class Inventory:
    """
    Represents an inventory that can hold items.

    Attributes:
        items (set): A set containing the items in the inventory.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.items = set()

    def add_item(self, item: Item) -> None:
        """
        Adds an item to the inventory.

        Args:
            item (Item): The item to add.
        """
        self.items.add(item)

    def remove_item(self, item: Item) -> None:
        """
        Removes an item from the inventory.

        Args:
            item (Item): The item to remove.
        """
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item.name} n'est pas dans l'inventaire.")

    def get_inventory(self) -> str:
        """
        Returns a string representation of the inventory.

        Returns:
            str: A formatted string listing the items in the inventory.
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
        Checks if the inventory is empty.

        Returns:
            bool: True if the inventory is empty, False otherwise.
        """
        return len(self.items) == 0
    

    def get_item_by_name(self, name: str) -> Item | None:
        """
        Finds an item in the inventory by its name.

        Args:
            name (str): The name of the item.

        Returns:
            Item | None: The item if found, None otherwise.
        """
        for item in self.items:
            if item.name == name:
                return item
        return None
