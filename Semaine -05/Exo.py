
# Partie 1 — Fichiers & gestion d'erreurs (10 points)
import json
# Crée un fichier utilisateurs.json contenant une liste de 4 utilisateurs (dictionnaires avec nom et code_acces)
utilisateurs = [
    {"nom":"jean", "code":1112},
    {"nom":"marc", "code":4486},
    {"nom":"ida", "code":9732},
    {"nom":"sarah", "code":7849}
]
with open("utilisateurs.json", "w") as f:
    json.dump(utilisateurs, f)
print("fichier créer !")

# Relis le fichier et affiche tous les utilisateurs
with open("utilisateurs.json", "r") as f:
    contenu = json.load(f)
    for ligne in contenu:
        print(ligne)


# Sauvegarde uniquement les noms dans noms_utilisateurs.txt
with open("nom_utilisateurs.txt", "w") as f:
    for utilisateur in utilisateurs:
        f.write(f"{utilisateur['nom']}\n")
    print("nom sauvegarder !")

    
# Relis ce fichier et affiche chaque nom (attention à ne pas répéter l'erreur read() + boucle for vue au dernier exo !)
with open("nom_utilisateurs.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
    
        


# Demande à l'utilisateur de taper un code d'accès (nombre). Gère avec try/except le cas où il tape du texte au lieu d'un nombre.
try:
    code = int(input("entrez un code: "))
    print(code)
except ValueError:
    print("Erreur ! entrez un nombre")


# Partie 2 — Modules math, random, datetime (10 points)
import math
import random
import datetime

# Utilise random pour générer un code d'accès aléatoire à 4 chiffres (entre 1000 et 9999) pour un nouvel utilisateur
password = random.randint(1000,9999)
print(f"le code généré est: {password}")

# Utilise math pour afficher la racine carrée de ce code généré
print(f"la racine carrée du code est: {math.sqrt(password)}")


# Utilise datetime pour :
# Afficher la date et l'heure actuelles de création de ce compte
date = datetime.date.today()
print(f"la date d'aujourd'hui est : {date}")
h = datetime.datetime.now()
print(f" il est {h.hour} heures:{h.minute} minutes:{h.second} secondes")


# Calculer et afficher combien de jours se sont écoulés depuis le 1er janvier de cette année
jour = datetime.date(date.year,1,1)
jour_ecoulé = (date - jour).days
print(f"le nombre de jour écoulé est de:{jour_ecoulé} jours")


# Partie 3 — Module os (10 points)
import os
# Affiche le dossier de travail actuel
print(os.getcwd())


# Crée un dossier comptes_utilisateurs/ (sans erreur si le dossier existe déjà)
os.makedirs("comptes_utilisateurs", exist_ok=True)
print("dossier créer !")
# Vérifie si ce dossier existe et affiche le résultat (True/False)
print(os.path.exists("comptes_utilisateurs"))


# Crée un fichier comptes_utilisateurs/dernier_compte.txt contenant le nom du nouvel utilisateur et son code d'accès généré
with open("comptes_utilisateurs/dernier_comptes.txt", "w") as f:
    mot = random.randint(1000,9999)
    f.write(f"nom: marie , code:{mot}\n")
    print("info ajoutée !")

# Vérifie que ce fichier existe et affiche sa taille en octets
print(os.path.exists("comptes_utilisateurs/dernier_comptes.txt"))
taille = os.path.getsize("comptes_utilisateurs/dernier_comptes.txt")
print(f"taille : {taille} octets")

# Partie 4 — Combinaison finale (5 points)

# Crée une fonction verifier_code(code_saisi, code_reel) (avec return) qui retourne "Accès autorisé" si les deux codes correspondent, sinon "Accès refusé
def verifier_code (code_saisi, code_reel):
    if code_saisi==code_reel:
        return("Accès autoriser")
    else:
        return("accès refusé") 

# Teste-la avec le code que l'utilisateur a saisi en Partie 1 et le code généré en Partie 2
print(verifier_code(code,password))


