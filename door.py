class Door:
    """
    Represents a door that can be locked or unlocked.
    """

    def __init__(self, locked=True):
        """
        Initializes the Door instance.

        Args:
            locked (bool): Whether the door is locked.
        """
        self.locked = locked

    def unlock(self, key_name: str) -> None:
        """
        Unlocks the door with the correct key.

        Args:
            key_name (str): The name of the key used.
        """
        if key_name == "key":
            self.locked = False
            print("La porte est maintenant déverrouillée.")
        else:
            print("Cette clé ne fonctionne pas ici.")

    def is_locked(self) -> bool:
        """
        Checks if the door is locked.

        Returns:
            bool: True if the door is locked, False otherwise.
        """
        return self.locked
