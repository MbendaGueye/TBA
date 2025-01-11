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

    def unlock(self, key_name):
        """
        Unlocks the door if the correct key is used.

        Args:
            key_name (str): The name of the key used.

        Returns:
            bool: True if the door was unlocked, False otherwise.
        """
        if key_name == "key":
            self.locked = False
            print("La porte du donjon est maintenant déverrouillée.")
            return True
        print("Vous ne pouvez pas déverrouiller cette porte avec cet objet.")
        return False

    def is_locked(self):
        """
        Checks if the door is locked.

        Returns:
            bool: True if the door is locked, False otherwise.
        """
        return self.locked
