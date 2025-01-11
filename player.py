from inventory import Inventory
from room import Room
from item import Item  # Import de la classe Item

class Player:
    """
    Represents the player in the game.
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
        Initializes the Player instance.

        Args:
            name (str): The name of the player.
        """
        self.name: str = name
        self.current_room: Room | None = None
        self.history: list[Room] = []
        self.inventory = Inventory()  # Initialize an empty inventory
        self.max_weight: float = max_weight



    def move(self, direction: str) -> bool:
        """
        Moves the player to a new room if possible.

        Args:
            direction (str): The direction to move in.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        normalized_direction = self.DIRECTIONS.get(direction.upper())
        if not normalized_direction:
            print(f"\n'{direction}' n'est pas une direction valide.\n")
            return False
        next_room = self.current_room.exits.get(normalized_direction)
        if not next_room:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self) -> str:
        """
        Returns the player's movement history.

        Returns:
            str: A formatted string of the player's movement history.
        """
        if not self.history:
            return "\nAucun lieu visité pour l'instant.\n"
        history_descriptions = [f"- {room.description}" for room in self.history]
        return "\nVous avez déjà visité les pièces suivantes :\n" + "\n".join(history_descriptions) + "\n"

    def add_item(self, item: Item) -> None:
        """
        Adds an item to the player's inventory.

        Args:
            item (Item): The item to add.
        """
        self.inventory.add_item(item)
        print(f"\n{item.name} a été ajouté à votre inventaire.\n")

    def remove_item(self, item: Item) -> None:
        """
        Removes an item from the player's inventory.

        Args:
            item (Item): The item to remove.
        """
        self.inventory.remove_item(item)
        print(f"\n{item.name} a été retiré de votre inventaire.\n")

    def get_inventory(self) -> str:
        """
        Returns the player's inventory as a string.

        Returns:
            str: A string representation of the inventory.
        """
        return self.inventory.get_inventory()

    def is_inventory_empty(self) -> bool:
        """
        Checks if the player's inventory is empty.

        Returns:
            bool: True if the inventory is empty, False otherwise.
        """
        return self.inventory.is_empty()
 
    def get_total_weight(self) -> float:
        """
        Returns the total weight of items in the player's inventory.
        """
        return sum(item.weight for item in self.inventory.items)

    def can_take_item(self, item: Item) -> bool:
        """
        Checks if the player can take the item without exceeding max_weight.

        Args:
            item (Item): The item to check.

        Returns:
            bool: True if the item can be taken, False otherwise.
        """
        return self.get_total_weight() + item.weight <= self.max_weight