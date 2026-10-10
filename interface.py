import math          #on en a besoin pour log2
import tkinter as tk

def calculer_entropie(mot_de_passe):
    longueur = len(mot_de_passe)

    # Mot de passe vide : on renvoie 0 au lieu de planter
    if longueur == 0:
        return 0

    a_minuscule = False
    a_majuscule = False
    a_chiffre = False
    a_symbole = False

    for caractere in mot_de_passe:
        if caractere.islower():
            a_minuscule = True
        elif caractere.isupper():
            a_majuscule = True
        elif caractere.isdigit():
            a_chiffre = True
        else:
            a_symbole = True

    taille_alphabet = 0
    if a_minuscule:
        taille_alphabet += 26
    if a_majuscule:
        taille_alphabet += 26
    if a_chiffre:
        taille_alphabet += 10
    if a_symbole:
        taille_alphabet += 33

    entropie = longueur * math.log2(taille_alphabet)
    return entropie


def donner_verdict(entropie):
    if entropie < 40:
        return "FAIBLE"
    elif entropie < 60:
        return "MOYEN"
    elif entropie < 80:
        return "FORT"
    else:
        return "TRÈS FORT"

def analyser():
    mot_de_passe = champ.get()                     #Lire
    entropie = calculer_entropie(mot_de_passe)     #Calculer
    verdict = donner_verdict(entropie)             #Juger
    resultat.config(text=f"Entropie : {round(entropie, 1)} bits\nVerdict : {verdict}")   #Afficher

fenetre = tk.Tk()
fenetre.title("Vérificateur de mot de passe")
fenetre.geometry("400x250")

titre = tk.Label(fenetre, text="Testez votre mot de passe", font=("Arial", 16))
titre.pack(pady=10)

champ = tk.Entry(fenetre, show="*", width=30)
champ.pack(pady=5)

bouton = tk.Button(fenetre, text="Analyser", command=analyser)   #command=analyser
bouton.pack(pady=10)

resultat = tk.Label(fenetre, text="", font=("Arial", 12))   #la zone de réponse
resultat.pack(pady=10)                                       

fenetre.mainloop()