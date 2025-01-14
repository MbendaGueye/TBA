"""
Module contenant la classe Item, qui représente un objet dans le jeu.
"""


class Item:
    """
    Représente un objet que le joueur peut trouver et utiliser dans le jeu.

    Attributs:
        name (str): Le nom de l'objet.
        description (str): Une description détaillée de l'objet.
        weight (float): Le poids de l'objet en kilogrammes.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Initialise une instance de Item.

        Args:
            name (str): Le nom de l'objet.
            description (str): La description de l'objet.
            weight (float): Le poids de l'objet.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de l'objet.

        Returns:
            str: Une chaîne formatée décrivant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
