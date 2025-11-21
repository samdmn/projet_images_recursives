#DEMON Samuel MI11
# BERHOUM Imad MI11
# Projet d'AP du 2nd semestre : Les images bitmap


import math
from PIL import Image, ImageDraw


def moyenne_couleur(coordonnees_hg : tuple[int], coordonnees_bd : tuple[int], image : Image) -> tuple[int] :
    """Calcule la couleur moyenne d'une image.
    
    Précondition : coordonnees_bd <= taille de l'image
    
    Exemple(s):
    $$$ im = Image.open('images/calbuth.png')
    $$$ im_rgb = im.convert('RGB')
    $$$ moyenne_couleur((0,0),(256,256), im_rgb)
    (140, 112, 73)
    $$$ moyenne_couleur((0,0),(128,128), im_rgb)
    (167, 148, 93)
    
    """
    rouge, vert, bleu = 0, 0, 0
    nb_pixels = (coordonnees_bd[0] - coordonnees_hg[0]) * (coordonnees_bd[1] - coordonnees_hg[1])
    for i in range(coordonnees_hg[0], coordonnees_bd[0]):
        for j in range(coordonnees_hg[1], coordonnees_bd[1]):
            r, v, b = image.getpixel((i, j))
            rouge += r
            vert += v
            bleu += b
    return (rouge//nb_pixels, vert//nb_pixels, bleu//nb_pixels)


def distance_couleur(couleur1 : tuple[int], couleur2 : tuple[int]):
    """Renvoie la distance euclidienne (vue en option DATA) entre 2 couleurs.

    Précondition : les couleurs doivent être des triplets (r,v,b)
    
    Exemple(s):
    $$$ distance_couleur((123,123,123),(123,123,123))
    0
    $$$ distance_couleur((123,123,123),(123,123,124))
    1
    
    """
    return math.sqrt((couleur1[0] - couleur2[0])**2 + (couleur1[1] - couleur2[1])**2 + (couleur1[2] - couleur2[2])**2)


def couleurs_proches(couleur1 : tuple[int], couleur2 : tuple[int], seuil : int) -> bool:
    """En fonction du seuil donné, renvoie True si les 2 couleurs sont proches, False sinon.

    Précondition : seuil >= 0 ; les couleurs doivent être des triplets (r,v,b)
    
    Exemple(s):
    $$$ couleurs_proches((123,123,123),(123,123,123),10)
    True
    $$$ couleurs_proches((123,123,123),(123,123,123),0)
    True
    $$$ couleurs_proches((123,123,123),(123,123,124),10)
    True
    $$$ couleurs_proches((123,123,123),(123,123,124),0)
    False
    
    """
    distance = distance_couleur(couleur1, couleur2)
    return distance <= seuil

# ---------- fonctions rédigées pour le projet mais qui au final s'avèrent inutiles------------

# def liste_couleurs_image(image : Image):
#     """à_remplacer_par_ce_que_fait_la_fonction
# 
#     Précondition : 
#     Exemple(s) :
#     $$$ 
# 
#     """
#     largeur, hauteur = image.size
#     liste_couleur = []
#     for ligne in range(largeur):
#         for colonne in range(hauteur):
#             liste_couleur.append(im_rgb.getpixel((ligne, colonne)))
#     return liste_couleur

# def moyenne_4_couleurs(couleur1 : tuple[int], couleur2 : tuple[int], couleur3 : tuple[int], couleur4 : tuple[int]) -> tuple[int]:
#     rouge=(couleur1[0]+couleur2[0]+couleur3[0]+couleur4[0])//4
#     vert=(couleur1[1]+couleur2[1]+couleur3[1]+couleur4[1])//4
#     bleu=(couleur1[2]+couleur2[2]+couleur3[2]+couleur4[2])//4
#     return (rouge,vert,bleu)
    