import tkinter as tk
racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500, height = 500, bg= "black")
canvas.create_line(250, 0, 250, 500, fill = "white")
racine.bind("<Button-1>", )
canvas.grid()
racine.mainloop()

cpt = 0
def alterne(event) : 
    global cpt
    if cpt % 2 == 0 :
        color = "white"
    else : 
        color = "black"
    cpt += 1
    canvas.itemconfigure(rectangle, fill = color)
    if cpt > 9 :
        racine.destroy()
