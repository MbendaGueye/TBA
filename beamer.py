from item import Item
from room import Room
from player import Player


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
        print(f"The Beamer '{self.name}' has been charged with the room '{room.name}'.")

    def use(self, player: Player) -> None:
        """
        Uses the Beamer to teleport the player to the charged room.

        Args:
            player (Player): The player using the Beamer.
        """
        if self.charged_room:
            player.current_room = self.charged_room
            print(f"You have been teleported to '{self.charged_room.name}'.")
            self.charged_room = None  # Reset the charge after use
        else:
            print("The Beamer is not charged.")
