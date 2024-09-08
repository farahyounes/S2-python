import tkinter as tk
import random

WIDTH, HEIGHT = 600, 600
import tkinter as tk
import random

WIDTH, HEIGHT = 600, 600
root=tk.Tk()
root.title("Mon dessin")
blackcanvas=tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')

objects=[]
color = "blue"  # Définition de la couleur par défaut

def cercle():
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    objects.append(blackcanvas.create_oval(x-50, y-50, x+50, y+50, fill=color))

def carre():
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    objects.append(blackcanvas.create_rectangle(x-50, y-50, x+50, y+50, fill=color))

def croix():
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    blackcanvas.create_line(x-50, y, x+50, y, fill=color, width=25)
    objects.append(blackcanvas.create_line(x, y-50, x, y+50, fill=color, width=25))

def choisircouleur():
    global color
    couleur = input("veillez choisir une couleur").lower()
    color = couleur

def undo():
    if objects:
        last_object = objects.pop()
        blackcanvas.delete(last_object)

#boutons 
button_couleur=tk.Button(root, text="choisir une couleur", fg='pink', font='georgia', command=choisircouleur)
button_cercle=tk.Button(root, text="cercle", command=cercle)
button_carre=tk.Button(root, text="carré", command=carre)
button_croix=tk.Button(root, text="croix", command=croix)
button_undo=tk.Button(root, text="undo", command=undo)

#affichage des boutons et canvas
blackcanvas.grid(row=1, rowspan=3, column=1)
button_undo.grid(row=0, column=2)
button_couleur.grid(row=0, column=1)
button_cercle.grid(row=1, column=0)
button_carre.grid(row=2, column=0)
button_croix.grid(row=3, column=0)

#fin du programme
root.mainloop()

