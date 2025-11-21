#DEMON Samuel MI11
# BERHOUM Imad MI11
# Projet d'AP du 2nd semestre : Les images bitmap

from PIL import Image, ImageDraw
from Couleur import moyenne_couleur, couleurs_proches, distance_couleur

class Bloc:
    def __init__(self, coordonnees_hg: tuple[int], coordonnees_bd: tuple[int], image : Image) -> None:
        """Initialise un bloc avec une image et ses coordonnées haut gauche (hg) et bas droite (bd).

        Précondition : image de taille puissance de 2 (256x256, 512x512, 1024x1024...)
        
        Exemple(s):
        
        # IMPORTANT : les tests sont menés avec l'image calbuth.png
        $$$ im = Image.open("images/calbuth.png")
        $$$ im_rgb = im.convert('RGB')
        $$$ a=Bloc((0,0),(256,256),im_rgb)
        $$$ a.coordonnees_bd
        (256, 256)
        $$$ a.couleur
        (140, 112, 73)
        $$$ a.sb1.couleur
        (167, 148, 93)
        $$$ a.sb1.coordonnees_bd
        (128, 128)
        $$$ a.est_uniforme()
        False
        $$$ a.sb1.sb1.sb1.sb1.est_uniforme()
        True
        """
        self.coordonnees_hg = coordonnees_hg
        self.coordonnees_bd = coordonnees_bd
        self.image = image
        self.couleur = moyenne_couleur(self.coordonnees_hg, self.coordonnees_bd, self.image)
        self.divise_bloc()
        

    def divise_bloc(self) -> None:
        """Divise le bloc en sous-blocs ou détermine la couleur si le bloc est uniforme.

        Précondition : bloc de taille puissance de 2 (256x256, 512x512, 1024x1024...)
        """
        if self.est_uniforme():
            self.couleur = moyenne_couleur(self.coordonnees_hg, self.coordonnees_bd, self.image)
        else:
            milieu_x = (self.coordonnees_hg[0] + self.coordonnees_bd[0]) // 2
            milieu_y = (self.coordonnees_hg[1] + self.coordonnees_bd[1]) // 2
                
            self.sb1 = Bloc(self.coordonnees_hg, (milieu_x, milieu_y), self.image)
            self.sb2 = Bloc((milieu_x, self.coordonnees_hg[1]), (self.coordonnees_bd[0], milieu_y), self.image)
            self.sb3 = Bloc((self.coordonnees_hg[0], milieu_y), (milieu_x, self.coordonnees_bd[1]), self.image)
            self.sb4 = Bloc((milieu_x, milieu_y), self.coordonnees_bd, self.image)
            

    def est_uniforme(self) -> bool:
        """Vérifie si le bloc est uniforme, c'est-à-dire si ses tous ses pixels sont de même couleur).

        Précondition : /
        """
        x_debut, y_debut = self.coordonnees_hg
        x_fin, y_fin = self.coordonnees_bd
        couleur_base = self.image.getpixel((x_debut, y_debut))
        for i in range(x_debut, x_fin):
            for j in range(y_debut, y_fin):
                if self.image.getpixel((i, j)) != couleur_base:
                    return False
        return True
    
    def colorer_moyenne(self) -> None:
        """Colore tous les pixels d'un bloc par la couleur moyenne des pixels de celui-ci.

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        dessin = ImageDraw.Draw(self.image)
        dessin.rectangle((self.coordonnees_hg,self.coordonnees_bd), fill = self.couleur)

        
    def __repr__(self):
        """Renvoie la représentation d'un bloc.

        Précondition : /
        """
        return f'Bloc({self.coordonnees_hg},{self.coordonnees_bd}, est_uniforme : {self.est_uniforme()}, couleur : {self.couleur})'
    