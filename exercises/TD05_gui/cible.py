#Importer tk
import tkinter as tk

#Créer la fenêtre racine et les variables inchangées
racine = tk.Tk()
COTE = 500
nb_cercle = 30
epaisseur = (COTE // 2 ) // nb_cercle

#Créer un canvas dans ma fenêtre racine 
canvas = tk.Canvas(racine, bg= "black", height = COTE, width = COTE)
canvas.grid()

#Créer un titre à ma fenêtre racine
racine.title("Cible qui fait mal aux yeux")

#liste des couleurs 
couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]

#Créer la forme 
for i in range(nb_cercle) :
    canvas.create_oval((epaisseur*i, epaisseur*i ), (COTE-epaisseur*i, COTE-epaisseur*i), fill =couleurs[i % len(couleurs)], outline = couleurs[i % len(couleurs)])
#Lancement de la boucle principale 
racine.mainloop()