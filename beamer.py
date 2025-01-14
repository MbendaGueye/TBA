from item import Item
from room import Room


class Beamer(Item):
    """
    A magical item that allows teleportation to a previously visited room.

    Attributes:
        charged_room (Room | None): The room where the Beamer is charged.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Initializes the Beamer.

        Args:
            name (str): The name of the Beamer.
            description (str): A description of the Beamer.
            weight (float): The weight of the Beamer.
        """
        super().__init__(name, description, weight)
        self.charged_room: Room | None = None

    def charge(self, room: Room) -> None:
        """
        Charges the Beamer with a specific room.

        Args:
            room (Room): The room to charge the Beamer with.
        """
        self.charged_room = room
        print(f"\nLe Beamer '{self.name}' est chargé avec la pièce '{room.name}'.\n")
