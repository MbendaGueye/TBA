from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.used_directions = set()  # Ensemble des directions utilisées

    def setup(self):
        # Setup commands
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)

        # Setup rooms
        forest = Room("Forest", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        tower = Room("Tower", "une immense tour en pierre qui s'élève au-dessus des nuages.")
        cave = Room("Cave", "une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        cottage = Room("Cottage", "un petit chalet pittoresque avec un toit de chaume.")
        swamp = Room("Swamp", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        castle = Room("Castle", "un énorme château fort avec des douves et un pont-levis.")
        dungeon = Room("Dungeon", "un donjon sombre et effrayant rempli de mystères.")
        sky_room = Room("Sky Room", "une salle lumineuse au sommet de la tour, offrant une vue magnifique.")

        self.rooms.extend([forest, tower, cave, cottage, swamp, castle, dungeon, sky_room])

        # Create exits for rooms
        forest.exits = {"N": cave, "S": castle}
        tower.exits = {"N": cottage, "S": swamp, "U": sky_room}
        cave.exits = {"S": forest, "E": cottage}
        cottage.exits = {"S": tower, "O": cave}
        swamp.exits = {"N": tower, "O": castle}
        castle.exits = {"N": forest, "E": swamp, "D": dungeon}
        dungeon.exits = {"U": castle}
        sky_room.exits = {"D": tower}

        # Récupérer les directions utilisées
        for room in self.rooms:
            self.used_directions.update(room.exits.keys())
        print(f"Directions utilisées dans le jeu : {self.used_directions}")

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    def play(self):
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string):
        list_of_words = command_string.split()
        if not list_of_words:
            return
        command_word = list_of_words[0]
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir les commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    Game().play()


if __name__ == "__main__":
    main()
