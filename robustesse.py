import math  #la boîte à outils mathématiques de Python
import math
import sys

mot_de_passe = input("Entrez un mot de passe : ")


longueur = len(mot_de_passe)

# Validation : on refuse un mot de passe vide (sinon log2(0) fait planter)
if longueur == 0:
    print("Vous n'avez rien tapé. Relancez le programme et entrez un mot de passe.")
    sys.exit()
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



taille_alphabet = 0

if a_minuscule:
    taille_alphabet += 26
if a_majuscule:
    taille_alphabet += 26
if a_chiffre:
    taille_alphabet += 10
if a_symbole:
    taille_alphabet += 33

print("Taille de l'alphabet :", taille_alphabet)

# Nombre total de combinaisons possibles
combinaisons = taille_alphabet ** longueur

print("Nombre de combinaisons possibles :", combinaisons)

entropie = longueur * math.log2(taille_alphabet)

print("Entropie :", round(entropie, 1), "bits")


if entropie < 40:
    print("Verdict : FAIBLE")
elif entropie < 60:
    print("Verdict : MOYEN")
elif entropie < 80:
    print("Verdict : FORT")
else:
    print("Verdict : TRÈS FORT")