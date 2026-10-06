mot_de_passe = input("Entrez un mot de passe : ")

longueur = len(mot_de_passe)
print("Votre mot de passe contient", longueur, "caractères.")

# On prépare 4 cases à cocher, toutes vides au départ
a_minuscule = False
a_majuscule = False
a_chiffre = False
a_symbole = False

# On regarde chaque caractère, un par un
for caractere in mot_de_passe:
    if caractere.islower():
        a_minuscule = True
    elif caractere.isupper():
        a_majuscule = True
    elif caractere.isdigit():
        a_chiffre = True
    else:
        a_symbole = True

# On affiche ce qu'on a trouvé
print("Contient des minuscules :", a_minuscule)
print("Contient des majuscules :", a_majuscule)
print("Contient des chiffres   :", a_chiffre)
print("Contient des symboles   :", a_symbole)