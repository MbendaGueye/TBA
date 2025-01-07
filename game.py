from room import Room
from player import Player
from command import Command
from actions import Actions
from typing import List, Dict, Set, Optional


class Game:
    """Represents the game logic and setup."""

    def __init__(self):
        self.finished: bool = False
        self.rooms: List[Room] = []
        self.commands: Dict[str, Command] = {}
        self.player: Optional[Player] = None
        self.used_directions: Set[str] = set()

    def setup(self) -> None:
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction> : se déplacer dans une direction", Actions.go, 1)
        self.commands["history"] = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["back"] = Command("back", " : revenir à la pièce précédente", Actions.back, 0)

        # Setup rooms
        forest = Room("Forest", "une forêt enchantée.")
        tower = Room("Tower", "une immense tour en pierre.")
        cave = Room("Cave", "une grotte sombre.")
        cottage = Room("Cottage", "un petit chalet pittoresque.")
        swamp = Room("Swamp", "un marécage sombre.")
        castle = Room("Castle", "un château fort.")
        dungeon = Room("Dungeon", "un donjon sombre.")
        sky_room = Room("Sky Room", "une salle lumineuse.")

        self.rooms.extend([forest, tower, cave, cottage, swamp, castle, dungeon, sky_room])
        forest.exits = {"N": cave, "S": castle}
        tower.exits = {"N": cottage, "S": swamp, "U": sky_room}
        cave.exits = {"S": forest, "E": cottage}
        cottage.exits = {"S": tower, "O": cave}
        swamp.exits = {"N": tower, "O": castle}
        castle.exits = {"N": forest, "E": swamp, "D": dungeon}
        dungeon.exits = {"U": castle}
        sky_room.exits = {"D": tower}

        for room in self.rooms:
            self.used_directions.update(room.exits.keys())
        print(f"Directions utilisées dans le jeu : {self.used_directions}")

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    def play(self) -> None:
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string: str) -> None:
        list_of_words = command_string.split()
        if not list_of_words:
            return
        command_word = list_of_words[0]
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir les commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self) -> None:
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    Game().play()


if __name__ == "__main__":
    main()
