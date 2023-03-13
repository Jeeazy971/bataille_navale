import random

# Constantes
TAILLE_GRILLE = 10
BATEAUX = {"Porte-avions": 5, "Croiseur": 4, "Destroyer": 3, "Sous-marin": 3, "Torpilleur": 2}
SYMBOLS = {"vide": "·", "bateau": "■", "touche": "X", "coule": "O"}


# Fonctions
def initialiser_grille():
    grille = []
    for i in range(TAILLE_GRILLE):
        ligne = []
        for j in range(TAILLE_GRILLE):
            ligne.append(SYMBOLS["vide"])
        grille.append(ligne)
    return grille


def afficher_grille(grille):
    print("  ", end="")
    for i in range(TAILLE_GRILLE):
        print(i, end=" ")
    print()
    for i in range(TAILLE_GRILLE):
        print(i, end=" ")
        for j in range(TAILLE_GRILLE):
            print(grille[i][j], end=" ")
        print()



def placer_bateaux(grille):
    for nom, taille in BATEAUX.items():
        bateau_place = False
        while not bateau_place:
            x = random.randint(0, TAILLE_GRILLE - 1)
            y = random.randint(0, TAILLE_GRILLE - 1)
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                if y + taille > TAILLE_GRILLE:
                    continue
                bateau = grille[x][y:y+taille]
                if SYMBOLS["bateau"] in bateau:
                    continue
                for i in range(taille):
                    grille[x][y+i] = SYMBOLS["bateau"]
            else:
                if x + taille > TAILLE_GRILLE:
                    continue
                bateau = [grille[i][y] for i in range(x, x + taille)]
                if SYMBOLS["bateau"] in bateau:
                    continue
                for i in range(taille):
                    grille[x+i][y] = SYMBOLS["bateau"]
            bateau_place = True


def tirer(grille, x, y):
    if grille[x][y] == SYMBOLS["vide"]:
        grille[x][y] = SYMBOLS["touche"]
        resultat = "raté"
    elif grille[x][y] == SYMBOLS["bateau"]:
        grille[x][y] = SYMBOLS["coule"]
        resultat = "touché"
    else:
        resultat = "déjà touché"
    return resultat


# Code principal
print("Bienvenue dans le jeu de bataille navale !")
grille_joueur = initialiser_grille()
grille_ordinateur = initialiser_grille()
placer_bateaux(grille_joueur)
placer_bateaux(grille_ordinateur)
afficher_grille(grille_joueur)

while True:
    # Tour du joueur
    print("C'est à votre tour de jouer.")
    x_joueur = int(input("Entrez la coordonnée x : "))
    y_joueur = int(input("Entrez la coordonnée y : "))
    resultat_joueur = tirer(grille_ordinateur, x_joueur, y_joueur)
    afficher_grille(grille_ordinateur)
    if all(SYMBOLS["bateau"] not in ligne for ligne in grille_ordinateur):
        print("Félicitations, vous avez gagné !")
        break
    if resultat_joueur == "raté":
        print("Vous avez raté votre tir.")
    elif resultat_joueur == "touché":
        print("Vous avez touché un bateau !")
    else:
        print("Vous avez déjà touché cette case.")

    # Tour de l'ordinateur
    print("C'est au tour de l'ordinateur.")
    x_ordinateur = random.randint(0, TAILLE_GRILLE - 1)
    y_ordinateur = random.randint(0, TAILLE_GRILLE - 1)
    resultat_ordinateur = tirer(grille_joueur, x_ordinateur, y_ordinateur)
    print("L'ordinateur tire en ({}, {}).".format(x_ordinateur, y_ordinateur))
    if all(SYMBOLS["bateau"] not in ligne for ligne in grille_joueur):
        print("L'ordinateur a gagné !")
        break
    if resultat_ordinateur == "raté":
        print("L'ordinateur a raté son tir.")
    elif resultat_ordinateur == "touché":
        print("L'ordinateur a touché l'un de vos bateaux !")
    else:
        print("L'ordinateur a déjà touché cette case.")
    afficher_grille(grille_joueur)
