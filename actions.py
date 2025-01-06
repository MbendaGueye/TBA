# Description: The actions module.

from room import Room

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O, U, D).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        player = game.player

        # Assurez-vous qu'une commande est fournie
        command_word = list_of_words[0] if list_of_words else "unknown"

        # Vérifiez le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=command_word))
            return False

        # Récupérer et normaliser la direction
        direction = list_of_words[1]
        normalized_direction = player.DIRECTIONS.get(direction.upper())

        if not normalized_direction:
            print(f"\n'{direction}' n'est pas une direction valide. Essayez N, E, S, O, U ou D.\n")
            return False

        # Déplacer le joueur
        if not player.move(normalized_direction):
            print("\nDéplacement impossible. Vérifiez les sorties disponibles.\n")
            return False

        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.
        """
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        """
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
