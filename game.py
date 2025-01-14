"""
Module principal contenant la logique du jeu d'aventure textuel.

Ce fichier définit la classe principale `Game` qui gère le déroulement du jeu, 
ainsi que l'initialisation des pièces, commandes, objets et personnages.
Le joueur peut interagir avec l'environnement en utilisant des commandes textuelles.
"""

from typing import List, Dict, Set, Optional
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from door import Door
from character import Character


class Game:
    """
    Représente la logique et la configuration du jeu.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de jeu.
        """
        self.finished: bool = False
        self.rooms: List[Room] = []
        self.commands: Dict[str, Command] = {}
        self.player: Optional[Player] = None
        self.used_directions: Set[str] = set()
        self.dungeon_door: Door = Door(locked=True)

    def setup(self) -> None:
        """
        Initialise les commandes, pièces, objets et portes du jeu.
        """
        # Ajout des commandes
        self.commands["help"] = Command(
            "help", " : afficher cette aide", Actions.help, 0
        )
        self.commands["quit"] = Command(
            "quit", " : quitter le jeu", Actions.quit, 0
        )
        self.commands["go"] = Command(
            "go", " <direction> : se déplacer", Actions.go, 1
        )
        self.commands["history"] = Command(
            "history", " : afficher l'historique", Actions.history, 0
        )
        self.commands["back"] = Command(
            "back", " : revenir à la pièce précédente", Actions.back, 0
        )
        self.commands["look"] = Command(
            "look", " : observer l'environnement", Actions.look, 0
        )
        self.commands["take"] = Command(
            "take", " <item_name> : prendre un objet", Actions.take, 1
        )
        self.commands["drop"] = Command(
            "drop", " <item_name> : déposer un objet", Actions.drop, 1
        )
        self.commands["check"] = Command(
            "check", " : vérifier l'inventaire", Actions.check, 0
        )
        self.commands["use"] = Command(
            "use", " <item_name> : utiliser un objet", Actions.use, 1
        )
        self.commands["talk"] = Command(
            "talk", " <character_name> : parler à un personnage", Actions.talk, 1
        )

        # Configuration des pièces
        forest = Room("Forest", "une forêt enchantée.")
        tower = Room("Tower", "une immense tour en pierre.")
        cave = Room("Cave", "une grotte sombre.")
        cottage = Room("Cottage", "un petit chalet pittoresque.")
        swamp = Room("Swamp", "un marécage sombre.")
        castle = Room("Castle", "un château fort.")
        dungeon = Room("Dungeon", "un donjon sombre.")
        sky_room = Room("Sky Room", "une salle lumineuse.")

        # Ajout d'objets aux pièces
        forest.inventory.add_item(Item("key", "une clé rouillée", 0.1))
        sky_room.inventory.add_item(Item("sword", "une épée au fil tranchant", 2.0))

        # Configuration des portes
        self.dungeon_door = Door(locked=True)
        castle.exits = {"N": forest, "E": swamp, "D": dungeon}
        dungeon.exits = {"U": castle}
        dungeon.door = self.dungeon_door

        # Sorties des pièces
        forest.exits = {"N": cave, "S": castle}
        tower.exits = {"N": cottage, "S": swamp, "U": sky_room}
        cave.exits = {"S": forest, "E": cottage}
        cottage.exits = {"S": tower, "O": cave}
        swamp.exits = {"N": tower, "O": castle}
        sky_room.exits = {"D": tower}

        # Ajout de personnages
        monster = Character(
            name="Monstre BOUBOU",
            description="un monstre effrayant",
            current_room=castle,
            synonyms=["monster", "monstre"],
        )
        princess = Character(
            name="Princesse Mbenda",
            description="une princesse en détresse",
            current_room=dungeon,
            synonyms=["princess", "princesse"],
        )
        castle.characters.append(monster)
        dungeon.characters.append(princess)

        # Stockage des pièces
        self.rooms.extend(
            [forest, tower, cave, cottage, swamp, castle, dungeon, sky_room]
        )

        for room in self.rooms:
            self.used_directions.update(room.exits.keys())

        print(f"Directions utilisées dans le jeu : {', '.join(self.used_directions)}")

        # Initialisation du joueur
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    def play(self) -> None:
        """
        Démarre la boucle principale du jeu.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string: str) -> None:
        """
        Traite une commande entrée par le joueur.

        Args:
            command_string (str): La commande entrée par le joueur.
        """
        list_of_words = command_string.split()
        if not list_of_words:
            return
        command_word = list_of_words[0]
        if command_word not in self.commands:
            print(
                f"\nCommande '{command_word}' non reconnue. "
                "Entrez 'help' pour voir les commandes disponibles.\n"
            )
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self) -> None:
        """
        Affiche le message de bienvenue pour le jeu.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    """
    Point d'entrée principal pour le jeu.
    """
    Game().play()


if __name__ == "__main__":
    main()
