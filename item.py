class Item:
    """
    Represents an item that can be found and used by the player in the game.

    Attributes:
        name (str): The name of the item.
        description (str): A detailed description of the item.
        weight (float): The weight of the item in kilograms.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Initializes an Item instance.

        Args:
            name (str): The name of the item.
            description (str): The description of the item.
            weight (float): The weight of the item.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self) -> str:
        """
        Returns a string representation of the item.

        Returns:
            str: A formatted string describing the item.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
