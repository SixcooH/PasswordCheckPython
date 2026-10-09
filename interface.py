import tkinter as tk

# 1. Construire la pièce : la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Vérificateur de mot de passe")
fenetre.geometry("400x250")

# 2. Un texte de titre
titre = tk.Label(fenetre, text="Testez votre mot de passe", font=("Arial", 16))
titre.pack(pady=10)

# 3. Le champ où l'utilisateur tape son mot de passe
champ = tk.Entry(fenetre, show="*", width=30)
champ.pack(pady=5)

# 4. Le bouton (il ne fait encore rien, c'est normal !)
bouton = tk.Button(fenetre, text="Analyser")
bouton.pack(pady=10)

# 5. Lancer la fenêtre
fenetre.mainloop()