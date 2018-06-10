# Introduction à `tkinter`

## Développement d’interfaces graphiques en Python 2

### *Luc Bertand, @Suponell*

---

# Importer le module

```python3
import Tkinter as tk
```

---

# Créer une fenêtre

```python
fenetre = tk.Tk()

# Configuration optionnelle
fenetre.title('Application tkinter')
fenetre.geometry(640, 360)  # Taille de la fenêtre

# TODO: Définir les objets

fenetre.mainloop()
```

---

# Les widgets

---

# Le `Label`

## Afficher du texte

```python
titre = tk.Label(fenetre, text='Application tkinter')
titre.pack()
```

---

# L’`Entry`

## Récupérer une saisie de l’utilisateur

```python
from time import sleep

nom = tk.Entry(fenetre)
nom.pack()

sleep(1)

print nom.get()
```

---

# Le `Button`

## Exécuter une action

```python
def calculer():
	print 3 * 5

bouton = Button(fenetre, text='Calculer',
		  command=calculer)
bouton.pack()
```

---

# Exemple de programme complet

*Code disponible sur mon [Github](https://github.com/Suponell/conferences/introduction-a-tkinter)*

---

```python
import Tkinter as tk

fenetre = tk.Tk()
fenetre.title('Convertisseur binaire')

entree = tk.Entry(fenetre)
entree.pack()

reponse = tk.Label(fenetre, text='0b')
reponse.pack()

def convertir():
	reponse.config(text=bin(int(entree.get())))

bouton = tk.Button(fenetre, text='Convertir',
		   command=convertir)
bouton.pack()

fenetre.mainloop()
```
