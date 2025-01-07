class Command:
    """
    Represents a command in the game.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help text for the command.
        action (function): The function to execute the command.
        number_of_parameters (int): The number of parameters expected by the command.
    """

    def __init__(self, command_word: str, help_string: str, action, number_of_parameters: int):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self) -> str:
        return f"{self.command_word}{self.help_string}"
