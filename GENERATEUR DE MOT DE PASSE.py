import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.iconbitmap(r'K:\test python\icone.ico')  # Remplace par le bon chemin si besoin
root.title("Générateur de mot de passe")

# Définir l'icône (assure-toi que le chemin est correct)
icon_path = os.path.join(os.getcwd(), 'icone.ico')
if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)

        # Pour forcer l'icône dans la barre des tâches aussi :
        # Crée une image transparente avec PIL
        img = Image.open(icon_path)
        img = img.resize((64, 64))  # Taille plus grande
        photo = ImageTk.PhotoImage(img)
        fake_label = tk.Label(root, image=photo)
        fake_label.image = photo
        root.iconphoto(True, photo)  # <- Cette ligne est clé pour la barre des tâches
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du chargement de l'icône : {e}")
else:
    messagebox.showwarning("Icône non trouvée", "Fichier 'icone.ico' non trouvé.")

# Le reste de ton interface ici
root.mainloop()
