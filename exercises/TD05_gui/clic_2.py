import tkinter as tk
racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500, height = 500, bg= "black")
canvas.create_line(250, 0, 250, 500, fill = "white")

def draw_cercle(event):
    x, y = event.x, event.y
    if event.x < 250:
        color = "blue"
    else : 
        color = "red"
    canvas.create_oval(x + 25, y + 25, x - 25, y -25, fill = color )


racine.bind("<Button-1>", draw_cercle)
canvas.grid()
racine.mainloop()

