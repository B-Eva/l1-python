#Importation 
from random import randint

#Fonction 
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    


def draw_pixel(i, j, color) :
    """colorie le pixel (i, j) du canvas de la couleur color."""
    canvas.create_line((i, j), (i+1, j), fill = color )



def ecran_aleatoire() :
    """remplit le canevas de manière à ce que chaque pixel soit d'une couleur choisie au hasard."""
    for i in range (256):
        for j in range (256):
            color = get_color(randint(0, 255), randint(0, 255), randint(0, 255))
            draw_pixel(i, j, color)


def degrade_gris() :
    for i in range (256):
        color = get_color(i, i, i) 
        for j in range(256) :
            draw_pixel(i, j, color)


def degrade_2D() :
    for i in range(256) :
        for j in range(256) :
            color = get_color(i, 0, j)
            draw_pixel(i, j, color)

#Importer tkinter
import tkinter as tk
#Créer une fenêtre racine
racine = tk.Tk()
#Titre de la fenêtre racine
racine.title("Travail sur les couleurs")
#Créer un canvas
canvas = tk.Canvas(racine, bg="black", height= 256, width = 256)
canvas.grid( row = 1, column = 1, rowspan = 3) #ATTENTION il ne faut pas oublier le grid ! Sinon pas de canvas ! rowspan veut dire que le canvas est disposé sur 3 lignes 
#Créer des bouttons 
b_alea = tk.Button( racine, command = ecran_aleatoire, text = "Aléatoire", font = ("helvetica", "20"), bg = "white", fg = "blue", padx = 10)
b_gris = tk.Button( racine, command = degrade_gris, text = "Dégradé gris", font = ("helvetica", "20"), bg = "white", fg = "blue", padx = 10)
b_2D = tk.Button( racine, command = degrade_2D, text = "Dégradé 2D", font = ("helvetica", "20"),  bg = "white", fg = "blue", padx= 10)
#Positionnement des boutons 
b_alea.grid( row = 1, column = 0)
b_gris.grid( row = 2, column = 0)
b_2D.grid( row = 3, column = 0)
#Lancement de la boucle principale 
racine.mainloop()