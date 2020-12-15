#EXERCICE 2

#Importer T
import tkinter as tk
import random as rd
ma_couleur = "blue"
objet = []


#Créer la fenêtre racine 
racine = tk.Tk()

#donner un titre à la fenêtre (racine)
racine.title("Mon dessin")

#Créer un canvas dans ma fenêtre (racine)
canvas = tk.Canvas(racine, bg = "black", height = 700, width = 700, relief = "raised", bd = 15)
canvas.grid(row=1, column=2)


#Créer des fonctions pour les bouttons 
def fct_cercle(b_cercle) :
    """Affiche un disque de diamètre 100, en bleu, placé aléatoirement sur le canvas lorsqu'on appuie sur le bouton correspondant"""
    x = rd.randint(0, 601)
    y = rd.randint(0, 601)
    objet.append(canvas.create_oval( (x, y), (x+100, y+100), fill = ma_couleur, ))

def fct_croix() :
    """Affiche une croix jaune dans un carré de côté 100, placé aléatoirement sur le canvas lorsqu'on appuie sur le bouton corrrespondant """
    x = rd.randint(0, 601)
    y = rd.randint(0, 601)
    objet.append(canvas.create_line((x, y), (x+100, y+100), fill = ma_couleur))
    objet.append(canvas.create_line((x+100, y), (x, y+100), fill = ma_couleur))
    

def fct_carre() :
    """Affiche un carré de côté 100, en rouge, placé aléatoirement sur le canvas lorsqu'on appuie sur le bouton correspondant"""
    x = rd.randint(0, 601)
    y = rd.randint(0, 601)
    objet.append(canvas.create_rectangle((x, y), (x+100, y+100), fill = ma_couleur))
    

def fct_couleur() :   
    """Demande à l'utilisateur dans le terminal de choisir uen couleur, les objets s'affichent de la couleur choisie, l'utilisateru peut demander autant de fois de couleur qu'il le souhaite"""
    global ma_couleur
    ma_couleur = input("Choisir une couleur :")

def undo() :
    global objet 
    if canvas.type(objet[-1]) == "line" :
        canvas.delete(objet[-1])
        del objet[-1]
        canvas.delete(objet[-1])
        del objet[-1]
    else : 
        canvas.delete(objet[-1])
        del objet[-1]
    return objet
    
         

    


#Créer des boutons dans ma fenêtre (racine) et les placer dans la fenêtre 
b_cercle = tk.Button(racine, text="Cercle", command = lambda : fct_cercle(b_cercle), font = ("helvetica", "15"), bg = "sandy brown", fg = "white", padx = 15)
b_carre = tk.Button(racine, text="Carré", command = fct_carre, font = ("helvetica", "15"), bg = "sandy brown", fg = "white", padx =15)
b_croix = tk.Button(racine, text="Croix", command = fct_croix, font=("helvetica", "15"), bg = "sandy brown", fg = "white", padx = 15)
b_couleur = tk.Button(racine, text="Choisir une couleur", command = fct_couleur,  font=("helvetica", "15"), bg = "white", fg = "black", padx = 15)
b_undo = tk.Button(racine, text = "undo", command = undo, font =("helvetica", "15"), bg = "black", fg = "white", padx = 15)
#Positoinnement des bouttons 
b_cercle.grid(row=0, column= 0)
b_carre.grid(row= 1, column= 0)
b_croix.grid(row= 2, column= 0)
b_couleur.grid(row= 0, column= 2)
b_undo.grid(row= 0, column = 3)

#Lancement de la boucle principale
racine.mainloop()

