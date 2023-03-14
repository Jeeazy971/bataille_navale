import random

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées, un tuple (no_ligne, no_colonne)
# un no_ligne ou no_colonne est compris dans le programme entre 1 et 10,
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')

TAILLE_GRILLE = 10

# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTRES = "ABCDEFGHIJ"


# chaque navire est constitué d'un dictionnaire dont les clés sont les
# coordonnées de chaque case le composant, et les valeurs correspondantes
# l'état de la partie du navire correspondant à la case
# (True : intact ; False : touché)

# les navires suivants sont disposés de façon fixe dans la grille :
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | o | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |

# détermination des coordonnées des cases voisines
def voisines(case):
    """
    Cette fonction renvoie la liste des coordonnées des cases voisines
    de la case passée en argument.
    """
    (ligne, colonne) = case
    liste_voisines = []
    for l in range(ligne - 1, ligne + 2):
        for c in range(colonne - 1, colonne + 2):
            if l >= 1 and l <= TAILLE_GRILLE and c >= 1 and c <= TAILLE_GRILLE:
                liste_voisines.append((l, c))
    liste_voisines.remove(case)
    return liste_voisines


# détermination des cases occupées par un navire

def cases_navire(navire):
    """
    Cette fonction renvoie la liste des coordonnées des cases occupées par
    le navire passé en argument.
    """
    cases = []
    for case in navire:
        cases.append(case)
        for voisine in voisines(case):
            if voisine in navire and voisine not in cases:
                cases.append(voisine)
    return cases


# vérification de la validité d'un navire

def navire_valide(navire):
    """
    Cette fonction renvoie True si le navire passé en argument est valide
    (c'est-à-dire si ses cases sont contiguës), False sinon.
    """
    if len(navire) == 0:
        return False
    cases = cases_navire(navire)
    for case in cases:
        for voisine in voisines(case):
            if voisine in cases:
                break
        else:
            return False
    return True


# vérification de la validité de la grille de jeu

def grille_valide(liste_navires):
    """
    Cette fonction renvoie True si la grille de jeu passée en argument est valide,
    False sinon.
    """
    # vérification de la validité des navires
    for navire in liste_navires:
        if not navire_valide(navire):
            return False
    # vérification de l'absence de superposition des navires
    cases_occupees = []
    for navire in liste_navires:
        for case in cases_navire(navire):
            if case in cases_occupees:
                return False
            cases_occupees.append(case)
    return True


# initialisation de la grille de jeu

while not grille_valide(liste_navires):
    # placement des navires
    porte_avion.clear()
    while not navire_valide(porte_avion):
        coordonnees = input("Placement du porte-avions (5 cases) : ")
        colonne = LETTRES.index(coordonnees[0].upper()) + 1
        ligne = int(coordonnees[1:])
        porte_avion = {(ligne, colonne + i): True for i in range(5)}
    croiseur.clear()
    while not navire_valide(croiseur):
        coordonnees = input("Placement du croiseur (4 cases) : ")
        colonne = LETTRES.index(coordonnees[0].upper()) + 1
        ligne = int(coordonnees[1:])
        croiseur = {(ligne, colonne + i): True for i in range(4)}
    contre_torpilleur.clear()
    while not navire_valide(contre_torpilleur):
        coordonnees = input("Placement du contre-torpilleur (3 cases) : ")


def placer_navires():
    """
    Place les navires dans la grille de jeu.
    """
    # Placement du porte-avion en B2 :
    for i in range(5):
        porte_avion[(2, i + 2)] = True

    # Placement du croiseur en A4 :
    for i in range(4):
        croiseur[(i + 1, 1)] = True

    # Placement du contre-torpilleur en C5 :
    for i in range(3):
        contre_torpilleur[(i + 3, 4)] = True

    # Placement du sous-marin en H5 :
    sous_marin[(5, 8)] = True
    sous_marin[(6, 8)] = True
    sous_marin[(7, 8)] = True

    # Placement du torpilleur en E9 :
    torpilleur[(9, 4)] = True
    torpilleur[(9, 5)] = True

    # Ajout des navires à la liste des navires :
    liste_navires.extend([porte_avion, croiseur, contre_torpilleur, sous_marin, torpilleur])


def jouer():
    """
    Joue une partie de bataille navale.
    """
    placer_navires()
    afficher_grille()

    while True:
        # Demande les coordonnées d'un tir au joueur :
        coordonnees_tir = demander_coordonnees_tir()

        # Vérifie si le tir touche un navire :
        navire_touche = None
        for navire in liste_navires:
            if coordonnees_tir in navire:
                navire_touche = navire
                navire[coordonnees_tir] = False  # Marque la case touchée
                break

        # Affiche le résultat du tir :
        if navire_touche is not None:
            print("Touché !")
        else:
            print("Dans l'eau !")

        # Vérifie si tous les navires ont été coulés :
        tous_coules = True
        for navire in liste_navires:
            if any(navire.values()):
                tous_coules = False
                break

        if tous_coules:
            print("Bravo, vous avez coulé tous les navires !")
            break

    print("Fin de la partie.")


# Lancement de la partie :
jouer()
