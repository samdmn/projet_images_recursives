# DEMON Samuel MI11 - BERHOUM Imad MI11

# Projet d'AP du 2nd semestre : Les images bitmap

## IMPORTANT

Il est évident que l'ensemble des scripts doivent être enregistrés dans le même dossier pour assurer le bon fonctionnement du programme principal. Les fichiers requis sont :

- `Bloc.py`
- `Couleur.py`
- `images_recursives.py` (et non pas images-recursives.py)

Toutes les fonctions sont documentées par une brève explication de leur utilité, une précondition et des tests (quand elles le permettent).

Il y a 2 façons de tester le programme principal :

- depuis la console de Thonny
- depuis le terminal en invite de commandes (expliqué dans le journal au 1 avril 2024)

Nous ne nous sommes pas répartis les tâches, nous avons préféré travailler à deux pour l'ensemble des fonctions ainsi que sur ce README. C'est pourquoi il n'est jamais précisé qui a fait telle fonction.



## Journal

### 7 mars 2024

Première lecture du sujet.
Découverte du module PIL et des fonctions à nombre variable de paramètres.
Début de l'implémentation de la classe Bloc (`__init__`, `est_uniforme`).

### 20 mars 2024

Suite de l'implémentation de la classe Bloc qui nécessite l'ajout de la fonction `moyenne_couleur` qui renvoie la moyenne des couleurs d'une image sous forme d'une tuple de trois entier (r,v,b) en prenant en paramètres ses coordonnées hauts gauches et bas droites (si jamais le bloc est uniforme).
Nous avons calculé les coordonnées des 4 sous-blocs d'un bloc dans le cas où le bloc de base ne serait pas uniforme.
Il reste encore à implémenter la fonction `est_uniforme`.

### 21 mars 2024

Implémentation de la fonction `est_uniforme` qui renvoie True si tous les pixels d'une image sont de la même couleur.
Malheureusement, nous finissons la séance du 21 mars bloqués par des erreurs de code probablement dûes à la récursivité utilisée dans le calcul des sous-blocs.

### 24 mars 2024

Relecture du sujet pour mieux comprendre les différentes fonctionnalités du projet (le processus pour pixelliser les images à l'aide des blocs nous parait encore un peu flou).
Nous choississons de créer un nouveau fichier `Couleur.py` où nous regroupons toutes les fonctions de calcul sur les couleurs.
Ainsi nous ajoutons la fonction `moyenne_couleur` dans ce fichier, et nous implémentons les fonctions :

- `liste_couleurs_image` qui renvoie la liste des triplets (r,v,b) de chaque pixel de l'image passée en paramètre.
- `distance_couleur` qui renvoie la distance euclidienne entre 2 couleurs.
- `couleurs_proches` qui, en fonction du seuil donné, renvoie True si les 2 couleurs sont proches et False sinon.

Le plus gros du travail reste à faire avec la classe Bloc qui est à terminer et les fonctions de manipulation d'images.

### 27 mars 2024

Nous avons finalisé la classe Bloc qui est maintenant fonctionnelle et dotée de 4 méthodes :

- `divise_bloc` qui divise le bloc en sous-blocs ou détermine la couleur si le bloc est uniforme.
- `est_uniforme` qui renvoie True si le bloc est uniforme, c'est-à-dire si ses tous ses pixels sont de même couleur).
- `colorer_moyenne` qui colore tous les pixels d'un bloc par la couleur moyenne des pixels de celui-ci.
- `__repr__` qui renvoie la représentation d'un bloc sous la forme `Bloc({self.coordonnees_hg},{self.coordonnees_bd},{self.couleur})`.

Évidemment, il y a aussi le `__init__` dans lequel on initialise les coordonnées, l'image et la couleur du bloc.
La couleur du bloc de départ est initialisée par la couleur moyenne de ses pixels.

Ensuite, nous implémentons les fonctions `bloc_to_image` et `image_to_blocs` qui nous serons utiles dans la fonction principale du projet.

### 28 mars 2024

Création de la "principale" fonction du projet que nous appelerons `images_recursives` qui prend en paramètres un bloc et un ordre (ici comme les images fournies sont de tailles 256x256 l'ordre maximal supporté est 8 (car 2^8 = 256), mais pour des images carrées plus grandes (1024x1024, 2048x2048) l'ordre pourra être supérieur à 8).
Pour réaliser cette fonction, nous suivons clairement à la lettre les consignes du projet.

Finalement, nous n'avons pas eu besoin d'utiliser les fontions `bloc_to_image` et `image_to_blocs`.

Une fois cette fonction créée, nous pouvons enfin avoir un rendu d'image bitmap à l'ordre voulu. Bien-sûr, nous essayons d'abord de pixelliser l'image de Calbuth en lançant dans la console ces tests :

- `a=Bloc((0,0),(256,256),im_rgb)`
- `b=image_recursive(a,5)`
- `im_rgb.show()`

ce qui nous donne le résultat suivant :

![img calbuth ordre 5](https://i.imgur.com/GZi2SBB.png)

Nous faisons en sorte de pouvoir changer l'image à pixelliser grâce à un input dans lequel l'utilisateur devra entrer le chemin vers l'image. De même pour l'ordre.

![img monkey ordre 6](https://i.imgur.com/0UkzSS0.png)

### 30 mars 2024

Pour lancer le programme depuis un terminal, il faut :

- Ouvrir le terminal
- se placer dans le dossier qui contient les scripts Python
- taper `python3 images_recursives.py`
- écrire le chemin de l'image à pixelliser
- écrire l'ordre

![img calbuth ordre 3 cmd](https://i.imgur.com/D8DWmYS.png)

### 1 avril 2024

Au final, nous décidons d'utiliser une invite de commande pour lancer le programme depuis le terminal. La méthode du 30 avril n'est donc plus valable mais est remplacée par une meilleure.

Pour se faire, il faut :

- Ouvrir le terminal
- se placer dans le dossier qui contient les scripts Python

L'invite de commande se présente sous la forme suivante : `python3 images_recursives.py nom_image nb_subdivisions`.

Par exemple, avec l'invite de commande `python3 images_recursives.py images/joconde.png 5` nous obtenons le résultat suivant :

![img joconde ordre 5 invite_commande](https://i.imgur.com/VQfOZSD.png)

Nous avons enlevé l'input qui permettait d'indiquer le chemin vers image. Par conséquent, pous initialiser un bloc, il faut maintenant définir une image manuellement dans la console :

- `im = Image.open("images/calbuth.png")`
- `im_rgb = im.convert('RGB')`
- `a=Bloc((0,0),(256,256),im_rgb)`

Nous n'avons malheureusement pas eu le temps de faire la partie "enregistrement d'une image dans un fichier".