"""
Module contenant la classe Command, utilisée pour représenter les commandes du jeu.

Chaque commande est associée à un mot-clé, un message d'aide, une action à exécuter,
et un nombre attendu de paramètres.
"""

class Command:
    """
    Représente une commande dans le jeu.

    Attributs:
        command_word (str): Le mot-clé de la commande.
        help_string (str): Le texte d'aide pour la commande.
        action (function): La fonction à exécuter lorsque la commande est appelée.
        number_of_parameters (int): Le nombre de paramètres attendus pour la commande.
    """

    def __init__(self, command_word: str, help_string: str, action, number_of_parameters: int):
        """
        Initialise une instance de Command.

        Args:
            command_word (str): Le mot-clé de la commande.
            help_string (str): Une description de la commande affichée pour aider l'utilisateur.
            action (function): La fonction associée à la commande.
            number_of_parameters (int): Le nombre de paramètres requis pour exécuter la commande.
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de la commande.

        Returns:
            str: Le mot-clé et le texte d'aide associés à la commande.
        """
        return f"{self.command_word}{self.help_string}"
