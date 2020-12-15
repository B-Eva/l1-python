import tkinter as tk
nb_clic = 0
point = (0, 0)

def draw_line(event) :
    global nb_clic, point
    if nb_clic == 0 : #première fois qu'on clique
        nb_clic = 1
        point = (event.x, event.y)
    else : 
        nb_clic = 0
        if (250 - event.x) * (250 - point[0]) >= 0 :
            color = "blue"
        else :
            color = "red"
        canvas.create_line(point, (event.x, event.y), fill = color)

canvas.create_line() #Finir de recopier