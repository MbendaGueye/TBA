from __future__ import annotations
from beamer import Beamer
from room import Room
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """
    Contains functions that execute commands in the game.
    """

    @staticmethod
    def go(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Moves the player in the specified direction.
        """
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
        """
        Quits the game.
        """
        print(f"\nMerci {game.player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Displays the list of available commands.
        """
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print(f"\t- {command.command_word}: {command.help_string}")
        print()
        return True

    @staticmethod
    def history(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Displays the player's movement history.
        """
        player = game.player
        print(player.get_history())
        return True

    @staticmethod
    def back(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Moves the player back to the previous room, if possible.
        """
        player = game.player
        if not player.history:
            print("\nAucun déplacement précédent. Vous êtes déjà à votre point de départ.\n")
            return False

        player.current_room = player.history.pop()
        print("\nVous êtes revenu dans une pièce précédente :")
        print(player.current_room.get_long_description())
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
        Displays the player's inventory.
        """
        player = game.player
        print(player.inventory.get_inventory())
        return True

    @staticmethod
    def take(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Takes an item from the room and adds it to the player's inventory.
        """
        player = game.player
        item_name = list_of_words[1]
        item = player.current_room.inventory.get_item_by_name(item_name)

        if not item:
            print(f"\nL'objet '{item_name}' n'est pas présent dans cette pièce.\n")
            return False

        if not player.can_take_item(item):
            print(f"\nVous ne pouvez pas prendre '{item_name}'. Le poids maximum serait dépassé.\n")
            return False

        player.add_item(item)
        player.current_room.inventory.remove_item(item)
        print(f"\nVous avez pris l'objet '{item_name}'.\n")
        return True

    @staticmethod
    def drop(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Drops an item from the player's inventory into the current room.
        """
        player = game.player
        item_name = list_of_words[1]
        item = player.inventory.get_item_by_name(item_name)

        if not item:
            print(f"\nVous ne possédez pas l'objet '{item_name}'.\n")
            return False

        player.remove_item(item)
        player.current_room.inventory.add_item(item)
        print(f"\nVous avez déposé l'objet '{item_name}'.\n")
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
            print(f"L'objet '{item_name}' n'est pas un Beamer.")
            return False

        beamer.charge(player.current_room)
        return True

    @staticmethod
    def use(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Uses an item in the player's inventory.
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
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.\n")
            return False

        # Utilisation de l'épée contre le monstre
        if item_name == "sword":
            monster = next(
                (char for char in current_room.characters if char.name.lower() == "monstre boubou"),
                None
            )
            if monster:
                print("\nVous avez tué le monstre avec SWORD !\n")
                current_room.characters.remove(monster)
                return True
            print("\nIl n'y a pas de monstre ici pour utiliser l'épée.\n")
            return False

        # Utilisation de la clé pour déverrouiller la porte du donjon
        if item_name == "key" and current_room.name == "Castle":
            dungeon_exit = current_room.exits.get("D")
            if dungeon_exit and dungeon_exit.door and dungeon_exit.door.is_locked():
                dungeon_exit.door.unlock(item_name)
                print("\nLa porte vers le donjon est maintenant déverrouillée.\n")
                return True
            print("\nLa porte vers le donjon est déjà déverrouillée.\n")
            return False

        print(f"\nL'objet '{item_name}' ne peut pas être utilisé ici.\n")
        return False

    @staticmethod
    def talk(game: Game, list_of_words: list[str], number_of_parameters: int) -> bool:
        """
        Interacts with a character in the current room.
        """
        player = game.player
        char_name = list_of_words[1].lower()
        current_room = player.current_room
        character = next((char for char in current_room.characters if char.matches_name(char_name)), None)

        if not character:
            print(f"\nIl n'y a aucun personnage nommé '{char_name}' ici.\n")
            return False

        # Condition spécifique pour la princesse
        if char_name in ["princess", "princesse"]:
            print("\nJEU GAGNÉ ! Vous avez sauvé la princesse ! Merci d'avoir joué !\n")
            game.finished = True
            return True

        # Utiliser la logique de conversation par défaut pour d'autres personnages
        message = character.talk(game)
        print(f"\n{message}\n")
        return not game.finished
