

# Projet TBA Mbenda Gueye


 Jeu de TBA python - Sauver la Princesse Mbenda
## Description du Projet

Ce jeu d'aventure textuel a pour objectif de vous immerger dans une quête captivante : sauver une princesse enfermée dans un donjon verrouillé. Attention, un monstre redoutable rôde dans le château où se trouve le donjon, et il faudra le vaincre pour accomplir votre mission.

### Scénario

- La princesse est enfermée dans un donjon verrouillé.
- Une clé rouillée est cachée dans une forêt enchantée pour déverrouiller le donjon.
- Un monstre terrifiant se trouve dans le château et doit être vaincu à l'aide d'une épée cachée dans une salle lumineuse.

Votre but est de :  
1. Explorer les différentes pièces.  
2. Trouver les objets nécessaires (clé et épée).  
3. Vaincre le monstre.  
4. Sauver la princesse.  

---

## Instructions d'Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/MbendaGueye/TBA.git
   ```

2. **Accéder au répertoire** :
   ```bash
   cd TBA
   ```


3. **dépendances** :
   Aucune dépendance externe n'est requise pour ce projet. Vous pouvez directement exécuter le jeu.

---

## Lancer le Jeu

1. Assurez-vous que vous êtes dans le répertoire principal contenant tous les fichiers `.py`.
2. Exécutez la commande suivante :
   ```bash
   python game.py
   ```
3. Suivez les instructions affichées à l'écran pour jouer.

## Carte du jeu:




## Commandes Disponibles

Pendant le jeu, vous pouvez utiliser les commandes suivantes :

| Commande        | Description                                         |
|-----------------|-----------------------------------------------------|
| `help`          | Affiche la liste des commandes disponibles.         |
| `go <direction>`| Se déplacer dans une direction (N, E, S, O, U, D). |
| `look`          | Observer l'environnement actuel.                   |
| `take <item>`   | Prendre un objet dans la pièce.                    |
| `drop <item>`   | Déposer un objet dans la pièce.                    |
| `use <item>`    | Utiliser un objet spécifique.                      |
| `talk <person>` | Parler à un personnage dans la pièce.              |
| `check`         | Vérifier l'inventaire.                             |
| `back`          | Revenir à la pièce précédente.                     |
| `history`       | Afficher l'historique des pièces visitées.         |
| `quit`          | Quitter le jeu.                                    |

---

## Structure des Fichiers

Voici les fichiers Python inclus dans ce projet, accompagnés de leurs descriptions :

### 1. **`game.py`**
   - Fichier principal contenant la logique du jeu.
   - Configure les pièces, objets et personnages.
   - Gère les commandes utilisateur et la boucle principale du jeu.

### 2. **`actions.py`**
   - Contient les actions disponibles dans le jeu (e.g., se déplacer, prendre un objet).
   - Définit les interactions possibles avec l'environnement.

### 3. **`room.py`**
   - Représente les pièces du jeu.
   - Gère les sorties, l'inventaire et les personnages présents dans chaque pièce.

### 4. **`player.py`**
   - Modélise le joueur.
   - Gère l'inventaire et les déplacements.

### 5. **`item.py`**
   - Définit les objets que le joueur peut collecter et utiliser.

### 6. **`door.py`**
   - Implémente une porte verrouillable que le joueur peut déverrouiller.

### 7. **`inventory.py`**
   - Modélise l'inventaire du joueur.
   - Permet d'ajouter, retirer et rechercher des objets.

### 8. **`character.py`**
   - Représente les personnages non-joueurs (NPC).
   - Implémente les interactions spécifiques, comme parler ou combattre.

### 9. **`command.py`**
   - Définit la structure des commandes du jeu.
   - Associe chaque commande à une action spécifique.

### 10. **`base_character.py`**
   - Classe de base pour les personnages, utilisée par `player.py` et `character.py`.

### 11. **`beamer.py`**
   - Un objet spécial qui permet de se téléporter dans une pièce précédemment visitée.

---

## Fonctionnalités Clés

- **Exploration** : Naviguez entre les pièces pour trouver des objets essentiels.
- **Interaction** : Parlez à des personnages et utilisez des objets.
- **Gestion d'inventaire** : Collectez et gérez des objets pour progresser.
- **Combat** : Vainquez le monstre pour atteindre le donjon.
- **Victoire** : Sauvez la princesse pour terminer le jeu !



## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer.

---

## Contribuer

Les contributions sont les bienvenues !

1. Forkez le dépôt.
2. Créez une branche pour vos modifications (`git checkout -b ma-branche`).
3. Commitez vos changements (`git commit -m "Ajout de nouvelles fonctionnalités"`).
4. Poussez vos modifications (`git push origin ma-branche`).
5. Créez une Pull Request.

---
© *Copyright Mbenda Gueye Esiee*
