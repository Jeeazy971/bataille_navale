# Ce programme est un jeu de bataille navale.
# Il utilise une grille de 10x10 cases.
# Les joueurs doivent placer des navires de différentes tailles sur la grille
# et tenter de couler tous les navires de l'adversaire en tirant sur des cases de la grille.

import random

TAILLE_GRILLE = 10

LETTRES = "ABCDEFGHIJ"

TOUCHE = False
INTACTE = True

# Définition des navires
liste_navires = ["porte_avion", "croiseur", "contre_torpilleur", "sous_marin", "torpilleur"]
porte_avion = {}
croiseur = {}
contre_torpilleur = {}
sous_marin = {}
torpilleur = {}

tirs = []
navires_coules = []


# Fonction pour demander les coordonnées au joueur
def demander_coordonnees():
    while True:
        coordonnees = input("Entrez les coordonnées (lettre,chiffre) ex: (A5) : ")
        if len(coordonnees) != 2 or coordonnees[0].upper() not in LETTRES or not coordonnees[1].isdigit():
            print("Coordonnées invalides, veuillez réessayer.")
        else:
            ligne = int(coordonnees[1])
            colonne = LETTRES.index(coordonnees[0].upper()) + 1
            if ligne < 1 or ligne > TAILLE_GRILLE or colonne < 1 or colonne > TAILLE_GRILLE:
                print("Coordonnées en dehors de la grille, veuillez réessayer.")
            else:
                return ligne, colonne


# Fonction pour placer les navires sur la grille
def placer_navire(navire, taille_navire):
    while True:
        print(f"Placement du navire de taille {taille_navire}")
        print(f"Entrez les coordonnées de la première case (lettre,chiffre) :")
        coordonnees = demander_coordonnees()
        ligne, colonne = coordonnees
        if colonne + taille_navire > TAILLE_GRILLE + 1:
            print("Le navire dépasse de la grille, veuillez réessayer.")
            continue
        for i in range(taille_navire):
            case = (ligne, colonne + i)
            navire[case] = INTACTE
        return


# Placement des navires sur la grille
tailles_navires = [5, 4, 3, 3, 2]
for i, navire in enumerate(liste_navires):
    placer_navire(eval(navire), tailles_navires[i])


# Fonction pour vérifier si le tir est un succès
def verifier_tir(ligne, colonne):
    for navire in liste_navires:
        if (ligne, colonne) in navire:
            navire[(ligne, colonne)] = TOUCHE
            if all(case == TOUCHE for case in navire.values()):
                navires_coules.append(navire)
                print("Vous avez coulé un navire !")
            else:
                print("Touché !")
                return True
    print("Dans l'eau...")
    return False


"""
Ici,j'ai fait une boucle while qui se répète tant que tous les navires n'ont pas été coulés. À chaque tour de boucle, 
j'affiche la grille de jeu, demande les coordonnées du tir au joueur, vérifie si le tir est valide, 
j'ajoute le tir à la liste des tirs effectués et, s'il touche un navire, 
je vérifié si le navire est coulé. 
Si tous les navires ont été coulés, j'affiche un message de victoire.

Il faut savoir que la fonction verifier_tir() est appelée deux fois dans cette boucle while, 
la première fois pour vérifier si le tir est valide (pour savoir s'il est dans l'eau ou touche un navire) 
et la deuxième fois pour vérifier si le navire est coulé. 
C'est pourquoi j'ai placé le code qui ajoute un navire à la liste des navires coulés dans la première condition, 
car si le navire est coulé, il ne sera plus dans la liste des navires et la deuxième condition échouera.
"""

while len(navires_coules) < len(liste_navires):
    print("\nGrille de jeu :")
    grille = []
    for i in range(TAILLE_GRILLE):
        ligne = []
        for j in range(TAILLE_GRILLE):
            if any((i + 1, j + 1) in navire for navire in navires_coules):
                ligne.append("X")
            elif (i + 1, j + 1) in tirs:
                if verifier_tir(i + 1, j + 1):
                    ligne.append("T")
                else:
                    ligne.append("O")
            else:
                ligne.append(".")
        grille.append(ligne)
    for ligne in grille:
        print(" ".join(ligne))
    print(f"Navires coulés : {[navire for navire in navires_coules]}")
    coordonnees = demander_coordonnees()
    if coordonnees in tirs:
        print("Vous avez déjà tiré ici, veuillez réessayer.")
    else:
        tirs.append(coordonnees)
        if verifier_tir(*coordonnees):
            print("Touché !")
            if all(case == TOUCHE for case in navire.values()):
                navires_coules.append(navire)
                print("Vous avez coulé un navire !")
            else:
                print("Dans l'eau...")
    print("Bravo, vous avez coulé tous les navires !")
