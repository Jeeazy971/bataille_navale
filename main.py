# Import de la librairie pour générer des nombres aléatoires
import random

# Définition de la taille de la grille de jeu
TAILLE_GRILLE = 10

# Définition de la liste des lettres utilisées pour identifier les colonnes
LETTRES = "ABCDEFGHIJ"

# Définition des constantes pour les différentes parties des navires
TOUCHE = False
INTACTE = True

# Initialisation de la liste des navires
liste_navires = ["porte_avion", "croiseur", "contre_torpilleur", "sous_marin", "torpilleur"]

# Initialisation des dictionnaires pour chaque navire
porte_avion = {}
croiseur = {}
contre_torpilleur = {}
sous_marin = {}
torpilleur = {}


# Définition d'une fonction pour demander les coordonnées au joueur
def demander_coordonnees():
    while True:
        # Demande des coordonnées au joueur
        coordonnees = input("Entrez les coordonnées (lettre,chiffre) ex: (A5) : ")
        # Vérification des coordonnées saisies
        if len(coordonnees) != 2 or coordonnees[0].upper() not in LETTRES or not coordonnees[1].isdigit():
            print("Coordonnées invalides, veuillez réessayer.")
        else:
            # Conversion des coordonnées en entiers
            ligne = int(coordonnees[1])
            colonne = LETTRES.index(coordonnees[0].upper()) + 1
            # Vérification que les coordonnées sont dans la grille
            if ligne < 1 or ligne > TAILLE_GRILLE or colonne < 1 or colonne > TAILLE_GRILLE:
                print("Coordonnées en dehors de la grille, veuillez réessayer.")
            else:
                return (ligne, colonne)


# Définition d'une fonction pour placer un navire sur la grille
def placer_navire(navire, taille_navire):
    while True:
        # Demande des coordonnées de la première case
        print(f"Placement du navire de taille {taille_navire}")
        print(f"Entrez les coordonnées de la première case (lettre,chiffre) :")
        coordonnees = demander_coordonnees()
        ligne, colonne = coordonnees
        # Vérification que le navire rentre dans la grille
        if colonne + taille_navire > TAILLE_GRILLE + 1:
            print("Le navire dépasse de la grille, veuillez réessayer.")
            continue
        # Placement du navire
        for i in range(taille_navire):
            case = (ligne, colonne + i)
            navire[case] = INTACTE
        return


# Placement des navires sur la grille
tailles_navires = [5, 4, 3, 3, 2]
for i, navire in enumerate(liste_navires):
    placer_navire(eval(navire), tailles_navires[i])
    print(f"Navire de taille {tailles_navires[i]} placé !")

# Affichage de la grille
grille = []
for i in range(TAILLE_GRILLE):
    ligne = []
    for j in range(TAILLE_GRILLE):
        case = (i + 1, j + 1)
        if case in porte_avion:
            if porte_avion[case] == TOUCHE:
                ligne.append("X")
            else:
                ligne.append("P")
        elif case in croiseur:
            if croiseur[case] == TOUCHE:
                ligne.append("X")
            else:
                ligne.append("C")
        elif case in contre_torpilleur:
            if contre_torpilleur[case] == TOUCHE:
                ligne.append("X")
            else:
                ligne.append("T")
        elif case in sous_marin:
            if sous_marin[case] == TOUCHE:
                ligne.append("X")
            else:
                ligne.append("S")
        elif case in torpilleur:
            if torpilleur[case] == TOUCHE:
                ligne.append("X")
            else:
                ligne.append("T")
        else:
            ligne.append(".")
    grille.append(ligne)

# Affichage de la grille
print("  " + " ".join(LETTRES))
for i, ligne in enumerate(grille):
    print(f"{i + 1:2} {' '.join(ligne)}")
