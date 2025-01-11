from __future__ import annotations
from beamer import Beamer
from room import Room
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

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

    @staticmethod
    def look(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Displays the description of the current room and its inventory.
        """
        player = game.player
        player.current_room.look()
        return True

    @staticmethod
    def check(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Vérifie et affiche le contenu de l'inventaire du joueur.
        """
        player = game.player
        print(player.inventory.get_inventory())
        return True

    @staticmethod
    def take(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        item_name = list_of_words[1]
        item = player.current_room.inventory.get_item_by_name(item_name)

        if not item:
            print(f"L'objet '{item_name}' n'est pas présent dans cette pièce.")
            return False

        if not player.can_take_item(item):
            print(f"Vous ne pouvez pas prendre '{item_name}'. Le poids maximum serait dépassé.")
            return False

        player.inventory.add_item(item)
        player.current_room.inventory.remove_item(item)
        print(f"Vous avez pris l'objet '{item_name}'.")
        return True

    @staticmethod
    def drop(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        player = game.player
        item_name = list_of_words[1]
        item = player.inventory.get_item_by_name(item_name)

        if not item:
            print(f"Vous ne possédez pas l'objet '{item_name}'.")
            return False

        player.inventory.remove_item(item)
        player.current_room.inventory.add_item(item)
        print(f"Vous avez déposé l'objet '{item_name}'.")
        return True

    @staticmethod
    def charge(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Charges a Beamer with the current room.
        """
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            print("\nUsage: charge <item_name>\n")
            return False

        item_name = list_of_words[1]
        beamer = player.inventory.get_item_by_name(item_name)

        if not isinstance(beamer, Beamer):
            print(f"The item '{item_name}' is not a Beamer.")
            return False

        beamer.charge(player.current_room)
        return True

    @staticmethod
    def use(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Uses the key to unlock the dungeon only if the player is in the dungeon
        and the key is in the inventory.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print("\nUsage: use <item_name>\n")
            return False

        item_name = list_of_words[1].lower()
        player = game.player
        current_room = player.current_room

        # Vérifier que l'objet est dans l'inventaire
        item = player.inventory.get_item_by_name(item_name)
        if not item:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return False

        # Vérifier que l'objet est une clé et que le joueur est dans le donjon
        if item_name == "key" and current_room.name == "Dungeon":
            if current_room.door and current_room.door.is_locked():
                current_room.door.unlock(item_name)  # Déverrouille la porte
                print("La porte du donjon est maintenant déverrouillée.")
                print(current_room.get_long_description())  # Affiche la description complète
                return True
            else:
                print("La porte du donjon est déjà déverrouillée.")
                return False

        print(f"L'objet '{item_name}' ne peut pas être utilisé ici.")
        return False
