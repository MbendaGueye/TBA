from __future__ import annotations  # Pour les types retardés
from room import Room  # Pas besoin d'importer `Game` ici
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game  # Importation conditionnelle pour éviter les boucles

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """Contains functions that execute commands in the game."""

    @staticmethod
    def go(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        command_word = list_of_words[0] if list_of_words else "unknown"
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]
        normalized_direction = player.DIRECTIONS.get(direction.upper())
        if not normalized_direction:
            print(f"\n'{direction}' n'est pas une direction valide. Essayez N, E, S, O, U ou D.\n")
            return False

        if not player.move(normalized_direction):
            print("\nDéplacement impossible. Vérifiez les sorties disponibles.\n")
            return False

        return True

    @staticmethod
    def quit(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        print(player.get_history())
        return True

    @staticmethod
    def back(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        if not player.history:
            print("\nAucun déplacement précédent. Vous êtes déjà à votre point de départ.\n")
            return False

        player.current_room = player.history.pop()
        print(player.current_room.get_long_description())
        print(player.get_history())  # Affiche l'historique mis à jour
        return True
