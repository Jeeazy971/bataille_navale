# bataille_navale

Projet de bataille navale en python

Ce code est un jeu de bataille navale. Le joueur et l'ordinateur placent leurs bateaux aléatoirement sur une grille de 10x10 cases, puis s'affrontent en tirant sur les cases de l'autre joueur. Le premier joueur à couler tous les bateaux de l'autre joueur gagne.

Le code se compose de plusieurs parties :

    Les constantes :
        TAILLE_GRILLE : la taille de la grille de jeu.
        BATEAUX : un dictionnaire qui contient les noms et les tailles des bateaux à placer sur la grille.
        SYMBOLS : un dictionnaire qui associe des symboles à chaque élément de la grille (vide, bateau, touché, coulé).

    Les fonctions :
        initialiser_grille : crée une grille vide de la taille TAILLE_GRILLE x TAILLE_GRILLE et la renvoie.
        afficher_grille : affiche une grille passée en paramètre.
        placer_bateaux : place les bateaux aléatoirement sur la grille passée en paramètre en respectant les contraintes de taille et de non-collision avec d'autres bateaux déjà placés.
        tirer : prend en entrée une grille, les coordonnées d'un tir et renvoie le résultat du tir (touché, raté, déjà touché).

    Le code principal :
        Initialise les deux grilles pour le joueur et l'ordinateur.
        Place les bateaux aléatoirement sur chaque grille.
        Affiche la grille du joueur.
        Lance une boucle infinie pour que les joueurs puissent tirer tour à tour.
        Le joueur entre les coordonnées de son tir.
        Le résultat du tir est affiché et la grille de l'ordinateur est mise à jour.
        Si tous les bateaux de l'ordinateur ont été coulés, le joueur gagne et la boucle se termine.
        L'ordinateur choisit aléatoirement les coordonnées de son tir.
        Le résultat du tir est affiché et la grille du joueur est mise à jour.
        Si tous les bateaux du joueur ont été coulés, l'ordinateur gagne et la boucle se termine.
