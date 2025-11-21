# Images Récursives

Application Python développée dans le cadre du projet d'AP du semestre 1.  
Ce script permet de **pixelliser des images** par subdivision récursive en blocs pour créer des rendus artistiques de type bitmap.

**Auteurs :** Samuel DEMON - Imad BERHOUM

![Exemple : Calbuth Ordre 5](https://i.imgur.com/GZi2SBB.png)

## 🧪 Fonctionnalités

- **Subdivision récursive d'images** en blocs de couleurs uniformes selon un ordre spécifié.
- Support des **images carrées** de différentes tailles (256×256, 1024×1024, 2048×2048, etc.).
- **Calcul automatique de la couleur moyenne** pour chaque bloc afin de créer un effet pixellisé harmonieux.
- **Niveau de subdivision personnalisable** (ordre) pour contrôler l'intensité de la pixellisation :
  - Ordre 3 : fortement pixellisé
  - Ordre 5-6 : effet artistique équilibré
  - Ordre 8 : détail maximal (pour les images 256×256)
- **Interface en ligne de commande** pour un traitement facile par lots.

## 🖥️ Technologies

- **Langage :** Python  
- **Bibliothèque :** PIL/Pillow (pour la manipulation d'images)  
- **Plateforme :** Multiplateforme (Windows, Linux, macOS)

## 🚀 Démarrage

### Prérequis

Assurez-vous que Python et Pillow sont installés.

```bash
pip install Pillow
```

### Structure du projet

Assurez-vous que tous les fichiers requis sont dans le même répertoire :

- `Bloc.py` – Implémentation de la classe Bloc
- `Couleur.py` – Fonctions de calcul sur les couleurs
- `images_recursives.py` – Programme principal

### Lancer l'application

Clonez ce dépôt et lancez le programme :

```bash
git clone https://github.com/samdmn/images-recursives.git
cd images-recursives
python3 images_recursives.py images/calbuth.png 5
```

**Syntaxe de la commande :**
```bash
python3 images_recursives.py <chemin_image> <ordre_subdivision>
```

**Exemples :**
```bash
python3 images_recursives.py images/joconde.png 5
python3 images_recursives.py images/monkey.png 6
```

### ⚙️ Personnalisation

Vous pouvez facilement modifier :

- **L'ordre de subdivision** via l'argument en ligne de commande pour contrôler le niveau de pixellisation (1-8 pour les images 256×256).
- **Le seuil de distance de couleur** dans `Couleur.py` pour ajuster la détection d'uniformité des blocs.
- **Le traitement d'image** en modifiant les méthodes de la classe `Bloc` dans `Bloc.py`.

### 📝 Utilisation en console

Vous pouvez également utiliser le programme de manière interactive depuis la console Python :

```python
from PIL import Image
from Bloc import Bloc
from images_recursives import image_recursive

im = Image.open("images/calbuth.png")
im_rgb = im.convert('RGB')
a = Bloc((0,0), (256,256), im_rgb)
b = image_recursive(a, 5)
im_rgb.show()
```

---

### 📊 Galerie de résultats

**Joconde - Ordre 5 :**
![Joconde Ordre 5](https://i.imgur.com/VQfOZSD.png)

**Monkey - Ordre 6 :**
![Monkey Ordre 6](https://i.imgur.com/0UkzSS0.png)

**Calbuth - Ordre 3 :**
![Calbuth Ordre 3](https://i.imgur.com/D8DWmYS.png)