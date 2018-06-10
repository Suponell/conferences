"""Application de conversion en binaire avec interface graphique."""

import Tkinter as tk

fenetre = tk.Tk()
fenetre.title('Convertisseur binaire')

entree = tk.Entry(fenetre)
entree.pack()

reponse = tk.Label(fenetre, text='0b')
reponse.pack()

def convertir():
	"""Convertir en binaire le nombre entré et afficher le résultat."""
	reponse.config(text=bin(int(entree.get())))

bouton = tk.Button(fenetre, text='Convertir', command=convertir)
bouton.pack()

fenetre.mainloop()
