# bataille_navale
Projet de bataille navale en python

Ce code est un jeu de bataille navale. Voici un commentaire pour chaque partie du code :

    La première partie du code est une ligne d'importation de la bibliothèque random. Cette bibliothèque permet de générer des nombres aléatoires.

    Ensuite, on définit quelques constantes :

        TAILLE_GRILLE : une grille de jeu est un tableau carré de 10x10 cases, cette variable est donc définie à 10.

        BATEAUX : il s'agit d'un dictionnaire qui contient les noms et tailles des différents bateaux que les joueurs vont devoir placer sur la grille. Chaque nom de bateau est associé à une taille.

        SYMBOLS : il s'agit d'un dictionnaire qui contient les symboles à utiliser pour représenter les différentes cases de la grille. On a un symbole pour une case vide, un symbole pour une case avec un bateau, un symbole pour une case touchée et un symbole pour une case où un bateau a été coulé.

    Ensuite, on définit quelques fonctions utiles pour le jeu :

        initialiser_grille() : cette fonction crée et renvoie une grille de jeu vide. Elle est utilisée pour initialiser les grilles des joueurs en début de partie.

        afficher_grille(grille) : cette fonction prend en paramètre une grille de jeu et l'affiche à l'écran. Elle utilise les symboles définis dans SYMBOLS pour représenter les différentes cases de la grille.

        placer_bateaux(grille) : cette fonction place les bateaux sur la grille. Elle parcourt le dictionnaire BATEAUX pour chaque bateau et le place sur la grille de manière aléatoire en vérifiant qu'il n'y a pas de chevauchement entre les bateaux déjà placés.

        tirer(grille, x, y) : cette fonction prend en paramètre une grille de jeu et les coordonnées d'un tir (x, y). Elle renvoie le résultat du tir ("raté", "touché" ou "déjà touché") et modifie la grille en conséquence (marque la case touchée ou coulée).

    La dernière partie du code est le code principal qui exécute le jeu. Voici ce qu'il fait :

        On affiche un message de bienvenue et on initialise les grilles des deux joueurs.

        On place les bateaux des deux joueurs sur leur grille respective en appelant la fonction placer_bateaux().

        On affiche la grille du joueur à l'écran.

        On entre dans une boucle infinie qui représente le tour par tour des joueurs.

        Pour chaque tour de jeu, on demande au joueur de saisir les coordonnées d'un tir (x, y). On effectue le tir en appelant la fonction tirer() sur la grille de l'adversaire.

        On affiche la grille de l'adversaire à l'écran pour montrer le résultat du tir.

        On vérifie si l'un des joueurs a gagné la partie (tous les bateaux de l'adversaire ont été coulés). Si c'est le cas, on affiche un message de victoire et on sort de la boucle
