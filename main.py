import random

# différentes états possibles pour une case de la grille de jeu
MER, TIR_RATE, TIR_TOUCHE, TIR_COULE = 0, 1, 2, 3

# taille de la grille de jeu
TAILLE_GRILLE = 10

# liste des différents types de navires à placer sur la grille de jeu
TYPES_NAVIRES = [
    {"nom": "porte-avions", "taille": 5},
    {"nom": "croiseur", "taille": 4},
    {"nom": "contre-torpilleur", "taille": 3},
    {"nom": "sous-marin", "taille": 3},
    {"nom": "torpilleur", "taille": 2},
]

# variable globale contenant la flotte de navires
flotte = []


def initialiser_flotte():
    """
    Initialise la flotte de navires avec des navires de tailles et de positions aléatoires sur la grille de jeu
    """
    global flotte
    flotte = []
    for navire_type in TYPES_NAVIRES:
        navire = placer_navire(navire_type["taille"])
        flotte.append(navire)


def placer_navire(taille):
    """
    Place un navire de la taille spécifiée sur la grille de jeu
    """
    while True:
        # choisir une position et une direction aléatoires pour le navire
        x = random.randint(0, TAILLE_GRILLE - 1)
        y = random.randint(0, TAILLE_GRILLE - 1)
        direction = random.choice(["horizontal", "vertical"])

        # vérifier si le navire peut être placé à cet endroit
        positions = []
        for i in range(taille):
            if direction == "horizontal":
                if x + i >= TAILLE_GRILLE:
                    break
                position = (x + i, y)
            else:
                if y + i >= TAILLE_GRILLE:
                    break
                position = (x, y + i)
            if position_deja_occupee(position):
                break
            positions.append(position)
        else:
            # le navire peut être placé à cet endroit
            for position in positions:
                ajouter_position_navire(position)
            return {"taille": taille, "positions": positions, "touche": [False] * taille}


def position_deja_occupee(position):
    """
    Vérifie si la position spécifiée est déjà occupée par un autre navire
    """
    for navire in flotte:
        if position in navire["positions"]:
            return True
    return False


def ajouter_position_navire(position):
    """
    Ajoute la position spécifiée à la liste des positions occupées par les navires
    """
    for navire in flotte:
        navire["positions"].append(position)


def demande_coord():
    """
    Demande les coordonnées d'un tir au joueur et les renvoie sous forme de tuple
    """
    while True:
        try:
            x = int(input("Entrez la coordonnée x (entre 0 et 9) : "))
            y = int(input("Entrez la coordonnée y (entre 0 et 9) : "))
            if 0 <= x < TAILLE_GRILLE and 0 <= y < TAILLE_GRILLE:
                return (x, y)
            print("Coordonnées invalides, veuillez réessayer.")
        except ValueError:
            print("Coordonnées invalides, veuillez réessayer.")


def afficher_grille(grille):
    """
    Affiche la grille de jeu
    """
    print(" 0123456789")
    for y in range(TAILLE_GRILLE):
        ligne = str(y) + " "
        for x in range(TAILLE_GRILLE):
            if grille[x][y] == MER:
                ligne += "~"
            elif grille[x][y] == TIR_RATE:
                ligne += "o"
            elif grille[x][y] == TIR_TOUCHE:
                ligne += "X"
            elif grille[x][y] == TIR_COULE:
                ligne += "#"
        print(ligne)


def jouer():
    """
    Fonction principale pour jouer une partie de bataille navale
    """
    print("Bienvenue dans la bataille navale !")
    initialiser_flotte()
    grille = [[MER] * TAILLE_GRILLE for _ in range(TAILLE_GRILLE)]
    nb_tirs = 0
    while True:
        afficher_grille(grille)
        coord = demande_coord()
        nb_tirs += 1
        if tirer(grille, coord):
            print("Touché !")
        if flotte_coulee():
            print("Vous avez coulé tous les navires en", nb_tirs, "tirs !")
            break
        else:
            print("Dans l'eau...")
    print("Merci d'avoir joué !")


def tirer(grille, coord):
    """
    Effectue un tir sur la grille de jeu aux coordonnées spécifiées.
    Renvoie True si un navire a été touché, False sinon.
    """
    x, y = coord
    if grille[x][y] == TIR_RATE or grille[x][y] == TIR_TOUCHE or grille[x][y] == TIR_COULE:
        print("Vous avez déjà tiré à cet endroit.")
        return False
    grille[x][y] = TIR_RATE
    for navire in flotte:
        if coord in navire["positions"]:
            navire["touche"][navire["positions"].index(coord)] = True
        if all(navire["touche"]):
            for position in navire["positions"]:
                grille[position[0]][position[1]] = TIR_COULE
                print("Coulé !")
            else:
                grille[x][y] = TIR_TOUCHE
                print("Touché !")
            return True
        return False


def flotte_coulee():
    """
    Vérifie si tous les navires de la flotte ont été coulés
    """
    for navire in flotte:
        if not all(navire["touche"]):
            return False
        return True


# jouer une partie
jouer()
