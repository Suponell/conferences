"""Application de conversion en binaire avec interface graphique."""

import Tkinter as tk

FENETRE = tk.Tk()
FENETRE.title('Convertisseur binaire')

ENTREE = tk.Entry(FENETRE)
ENTREE.pack()

REPONSE = tk.Label(FENETRE, text='0b')
REPONSE.pack()


def convertir():
    """Convertir en binaire le nombre entré et afficher le résultat."""
    REPONSE.config(text=bin(int(ENTREE.get())))


BOUTON = tk.Button(FENETRE, text='Convertir', command=convertir)
BOUTON.pack()

FENETRE.mainloop()
