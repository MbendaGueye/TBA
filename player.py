from room import Room


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

    def __init__(self, name: str):
        self.name: str = name
        self.current_room: Room | None = None
        self.history: list[Room] = []

    def move(self, direction: str) -> bool:
        """
        Moves the player to a new room if possible.
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
        """
        if not self.history:
            return "\nAucun lieu visité pour l'instant.\n"
        history_descriptions = [f"- {room.description}" for room in self.history]
        return "\nVous avez déjà visité les pièces suivantes :\n" + "\n".join(history_descriptions) + "\n"
