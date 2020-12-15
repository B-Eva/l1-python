import tkinter as tk
racine = tk.Tk()
racine.title("CLIC 1")

canvas = tk.Canvas(racine, bg = "black", height = 500, width = 500, relief = "raised", bd = 15)
canvas.grid()

def draw_pixel(i, j, color) :
    """colorie le pixel (i, j) du canvas de la couleur color."""
    canvas.create_line((i, j), (i+1, j), fill = color )

def affichage(event) : 
    draw_pixel(event.x, event.y, color = "red")

canvas.bind("<Button-1>", affichage)
racine.mainloop()
