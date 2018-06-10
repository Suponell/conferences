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
FENETRE = tk.Tk()

# Configuration optionnelle
FENETRE.title('Application tkinter')
FENETRE.geometry(640, 360)  # Taille de la fenêtre

# TODO: Définir les objets

FENETRE.mainloop()
```

---

# Les widgets

---

# Le `Label`

## Afficher du texte

```python
TITRE = tk.Label(FENETRE, text='Application tkinter')
TITRE.pack()
```

---

# L’`Entry`

## Récupérer une saisie de l’utilisateur

```python
from time import sleep

ENTREE = tk.Entry(FENETRE)
ENTREE.pack()

sleep(1)

print ENTREE.get()
```

---

# Le `Button`

## Exécuter une action

```python
def calculer():
	print 3 * 5

BOUTON = Button(FENETRE, text='Calculer',
		  command=calculer)
BOUTON.pack()
```

---

# Exemple de programme complet

*Code disponible sur mon [Github](https://github.com/Suponell/conferences/tree/master/introduction-a-tkinter)*

---

```python
"""Application de conversion en binaire avec interface
graphique.
"""

import Tkinter as tk

FENETRE = tk.Tk()
FENETRE.title('Convertisseur binaire')

ENTREE = tk.Entry(FENETRE)
ENTREE.pack()

REPONSE = tk.Label(FENETRE, text='0b')
REPONSE.pack()
````

---

```python
def convertir():
    """Convertir en binaire le nombre entré et afficher
    le résultat.
    """
    REPONSE.config(text=bin(int(ENTREE.get())))


BOUTON = tk.Button(FENETRE, text='Convertir',
	           command=convertir)
BOUTON.pack()

FENETRE.mainloop()
```

---

# Merci !
