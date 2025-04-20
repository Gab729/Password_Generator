import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import string

# Fonction pour générer un mot de passe
def generer_mot_de_passe():
    try:
        longueur = int(entry_longueur.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        return

    # Construire le jeu de caractères selon les cases cochées
    caractere_possibles = ""
    if var_lettres.get():
        caractere_possibles += string.ascii_letters
    if var_chiffres.get():
        caractere_possibles += string.digits
    if var_symboles.get():
        caractere_possibles += string.punctuation

    if not caractere_possibles:
        messagebox.showwarning("Erreur", "Veuillez sélectionner au moins une option.")
        return

    mot_de_passe = ''.join(random.choices(caractere_possibles, k=longueur))
    entry_mot_de_passe.delete(0, tk.END)
    entry_mot_de_passe.insert(0, mot_de_passe)

# Créer la fenêtre principale
root = tk.Tk()
root.state('zoomed')  # Plein écran Windows
root.iconbitmap(r'K:/test python/icone.ico')
root.title("Générateur de Mot de Passe")

# Charger l'image de fond
background_image = Image.open("K:/test python/1.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Label pour l'image de fond
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Widgets
label_longueur = tk.Label(root, text="Longueur du mot de passe:", bg="white", font=("Arial", 12))
label_longueur.pack(pady=10)

entry_longueur = tk.Entry(root, font=("Arial", 12), width=20)
entry_longueur.pack(pady=10)

# Variables pour les cases à cocher
var_lettres = tk.BooleanVar(value=True)
var_chiffres = tk.BooleanVar(value=True)
var_symboles = tk.BooleanVar(value=True)

# Cases à cocher
checkbox_lettres = tk.Checkbutton(root, text="Lettres (a-z, A-Z)", variable=var_lettres, bg="white", font=("Arial", 11))
checkbox_lettres.pack()

checkbox_chiffres = tk.Checkbutton(root, text="Chiffres (0-9)", variable=var_chiffres, bg="white", font=("Arial", 11))
checkbox_chiffres.pack()

checkbox_symboles = tk.Checkbutton(root, text="Symboles (!@#...)", variable=var_symboles, bg="white", font=("Arial", 11))
checkbox_symboles.pack()

# Résultat
label_mot_de_passe = tk.Label(root, text="Mot de passe généré:", bg="white", font=("Arial", 12))
label_mot_de_passe.pack(pady=10)

entry_mot_de_passe = tk.Entry(root, font=("Arial", 12), width=40)
entry_mot_de_passe.pack(pady=10)

# Bouton
button_generer = tk.Button(root, text="Générer le mot de passe", font=("Arial", 12), command=generer_mot_de_passe)
button_generer.pack(pady=20)

# Ajustement dynamique de l’image de fond
def ajuster_image():
    image = Image.open("K:/test python/1.jpg")
    image = image.resize((root.winfo_width(), root.winfo_height()), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    background_label.config(image=photo)
    background_label.image = photo  # Important

root.bind("<Configure>", lambda event: ajuster_image())

# Lancer l'interface
root.mainloop()
