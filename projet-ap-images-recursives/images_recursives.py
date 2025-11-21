#DEMON Samuel MI11
# BERHOUM Imad MI11
# Projet d'AP du 2nd semestre : Les images bitmap

from PIL import Image, ImageDraw
import math
from Bloc import Bloc
from Couleur import moyenne_couleur, couleurs_proches, distance_couleur

def image_recursive(bloc : Bloc, ordre : int) -> Image:
    """Algorithme d'image récursive qui modifie le contenu d'im_rgb par une image bitmap de l'ordre donné.

    Précondition : 2**ordre <= taille de l'image
    """
    if ordre != 0:
        milieu_x = (bloc.coordonnees_hg[0] + bloc.coordonnees_bd[0]) // 2
        milieu_y = (bloc.coordonnees_hg[1] + bloc.coordonnees_bd[1]) // 2
        
        sous_image1 = Bloc(bloc.coordonnees_hg, (milieu_x, milieu_y), bloc.image)
        sous_image2 = Bloc((milieu_x, bloc.coordonnees_hg[1]), (bloc.coordonnees_bd[0], milieu_y), im_rgb)
        sous_image3 = Bloc((bloc.coordonnees_hg[0], milieu_y), (milieu_x, bloc.coordonnees_bd[1]), im_rgb)
        sous_image4 = Bloc((milieu_x, milieu_y), bloc.coordonnees_bd, im_rgb)
        
        a = image_recursive(sous_image1, ordre-1)
        b = image_recursive(sous_image2, ordre-1)
        c = image_recursive(sous_image3, ordre-1)
        d = image_recursive(sous_image4, ordre-1)
        
        if couleurs_proches(a.couleur, b.couleur, 5) and couleurs_proches(c.couleur, d.couleur, 5):
            bloc.colorer_moyenne()
        
        else:
            bloc.sb1 = a
            bloc.sb2 = b
            bloc.sb3 = c
            bloc.sb4 = d
        
        return bloc
    
    else:
        bloc.colorer_moyenne()
        return bloc
    
def pixellise_image(bloc : Bloc, ordre : int) -> None:
    """affiche l'image à l'ordre pixellisé donné

    Précondition : /
    """
    image_recursive(bloc, ordre)
    im_rgb.show()
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: images_recursives.py image ordre")
    else:
        image, ordre = sys.argv[1:]
        if image in {"images/calbuth.png", "images/joconde.png", "images/galets.png", "images/monkey.jpg"}:
            image = str(image)
            ordre = int(ordre)
            im = Image.open(image)
            im_rgb = im.convert('RGB')
            bloc = Bloc((0,0),im_rgb.size,im_rgb)
            pixellise_image(bloc, ordre)



    
# ---------- fonctions rédigées pour le projet mais qui au final s'avèrent inutiles------------
    
# def bloc_to_image(bloc):
#     """à_remplacer_par_ce_que_fait_la_fonction
# 
#     Précondition : 
#     Exemple(s) :
#     $$$ 
# 
#     """
#     largeur = bloc.coordonnees_bd[0] - bloc.coordonnees_hg[0]
#     hauteur = bloc.coordonnees_bd[1] - bloc.coordonnees_hg[1]
#     image = Image.new("RGB", (largeur, hauteur))
# 
#     if bloc.couleur != None:
#         image.putpixel((0, 0), bloc.couleur)
#         for i in range(largeur):
#             for j in range(hauteur):
#                 image.putpixel((i, j), bloc.couleur)
#     else:
#         sb1_img = bloc_to_image(bloc.sb1)
#         sb2_img = bloc_to_image(bloc.sb2)
#         sb3_img = bloc_to_image(bloc.sb3)
#         sb4_img = bloc_to_image(bloc.sb4)
# 
#         image.paste(sb1_img, (0, 0))
#         image.paste(sb2_img, (largeur // 2, 0))
#         image.paste(sb3_img, (0, hauteur // 2))
#         image.paste(sb4_img, (largeur // 2, hauteur // 2))
#     return image
# 
# 
# def image_to_blocs(image, taille_bloc):
#     """à_remplacer_par_ce_que_fait_la_fonction
# 
#     Précondition : 
#     Exemple(s) :
#     $$$ 
# 
#     """
#     largeur, hauteur = image.size
#     
#     for i in range(0, hauteur, taille_bloc):
#         for j in range(0, largeur, taille_bloc):
#             coordonnees_hg = (j, i)
#             coordonnees_bd = (j + taille_bloc, i + taille_bloc)
#             coordonnees_bd = (min(coordonnees_bd[0], largeur), min(coordonnees_bd[1], hauteur))
#             bloc = Bloc(coordonnees_hg, coordonnees_bd, image) 
#     return bloc
# 
# def divise_en_4(bloc):
#     milieu_x = (bloc.coordonnees_hg[0] + bloc.coordonnees_bd[0]) // 2
#     milieu_y = (bloc.coordonnees_hg[1] + bloc.coordonnees_bd[1]) // 2
#     sous_image1 = Bloc(bloc.coordonnees_hg, (milieu_x, milieu_y), bloc.image)
#     sous_image2 = Bloc((milieu_x, bloc.coordonnees_hg[1]), (bloc.coordonnees_bd[0], milieu_y), im_rgb)
#     sous_image3 = Bloc((bloc.coordonnees_hg[0], milieu_y), (milieu_x, bloc.coordonnees_bd[1]), im_rgb)
#     sous_image4 = Bloc((milieu_x, milieu_y), bloc.coordonnees_bd, im_rgb)
#     return [sous_image1, sous_image2,sous_image3,sous_image4]

# if __name__ == "__main__":
#     ordre = input("ordre : ")
#     pixellise_image(Bloc((0,0),im_rgb.size,im_rgb), int(ordre))
    


    