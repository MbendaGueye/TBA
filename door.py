"""
Module contenant la classe Door, qui représente une porte dans le jeu.

La classe Door permet de gérer l'état d'une porte (verrouillée ou déverrouillée)
et fournit des méthodes pour interagir avec elle.
"""


class Door:
    """
    Représente une porte qui peut être verrouillée ou déverrouillée.

    Attributs:
        locked (bool): Indique si la porte est verrouillée.
    """

    def __init__(self, locked: bool = True):
        """
        Initialise une instance de Door.

        Args:
            locked (bool): Indique si la porte est verrouillée au départ. Par défaut, True.
        """
        self.locked = locked

    def unlock(self, key_name: str) -> None:
        """
        Déverrouille la porte avec la clé correcte.

        Args:
            key_name (str): Le nom de la clé utilisée.
        """
        if key_name == "key":
            self.locked = False
            print("La porte est maintenant déverrouillée.")
        else:
            print("Cette clé ne fonctionne pas ici.")

    def is_locked(self) -> bool:
        """
        Vérifie si la porte est verrouillée.

        Returns:
            bool: True si la porte est verrouillée, sinon False.
        """
        return self.locked
