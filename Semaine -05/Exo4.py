# Partie 1- Variables, conditions et boucles
nom = "La bouffe"
annee = 2023
nombres_table = 200
print(f"le restaurant {nom} ouvert en {annee} compte {nombres_table} tables")
if nombres_table > 20:
    print("grand restaurant")
else:
    print("petit restaurant")
spécialites = ["thiéboudienne","poulet yassa","aloko","kedjenou","attiéké"]
somme=0
for spécialité in spécialites:
    somme+=1
    print(f"{somme}:{spécialité}")
# Partie 2- Fonctions
def crer_plat(nom, prix, disponible=True):
    return {"nom":nom, "prix":prix, "disponible":disponible}
print(crer_plat("riz",2000,False))

def est_disponible(disponible):
    if disponible==True:
        return True
    else:
        return False
def calculer_addition(prix, personne = 1):
    addition = prix * personne
    return addition
def categorie_prix(prix):
    if prix<2000:
        return("économique")
    elif prix<5000:
        return("normal")
    else:
        return ("cher")
# Partie 3 - Listes de dictionnaires
plats =[
    crer_plat("thiéboudienne",5000,False),
    crer_plat("poulet yassa",3500),
    crer_plat("Aloko",1500,False),
    crer_plat("Kedjenou", 4000),
    crer_plat("Attiékè poisson",2500,False),
    crer_plat("Riz gras",2000)
]
for plat in plats:
    print(plat)
for plat in plats:
    if plat['disponible']==True:
        n = est_disponible(plat['disponible'])
        print(f"{plat['nom']}:{n}")
big = max (plats, key=lambda e:e['prix'])
print(f"{big['nom']}:{big['prix']}")
smole = min (plats, key=lambda e:e['prix'])
print(f"{smole['nom']}:{smole['prix']}")

somme = 0
moy = 0
for plat in plats:
    somme += plat['prix']
    moy = somme / len(plats)
print(f"somme:{somme}")
print(f"moyenne: {moy}")

# Partie 4 - Fichiers
import json
with open("menu.json", "w") as f:
    json.dump(plats,f)
print("fichier sauvegardé !")
with open("menu.json", "r") as f:
    contenu = json.load(f)
for ligne in contenu:
    print(ligne)
with open("plats.txt", "w") as f:
    for plat in plats: 
        f.write(f"{plat['nom']}\n")
print(f"fichier sauvegardé !")
with open ("plats.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
        
# Partie 5 - modules
import random
numéro_commande = random.randint(1000,9999)
print(f"numéro de commandes:{numéro_commande}")
import datetime
jour = datetime.date.today()
print(f"nous sommes le {jour}")

h = datetime.datetime.now()
print(f"il est {h.hour}:{h.minute}")

décembre = datetime.date(jour.year,12,31)
jour_restant = (décembre - jour).days
print(f" ils restent exactement {jour_restant} jours avant le 31 décembre")

import os
os.makedirs("commandes/", exist_ok=True)
print("dossier créer !")

import math

print(math.sqrt(numéro_commande))
print(math.ceil(numéro_commande))

# Partie 6 - Gestion des erreurs
try:
    prix = int(input("Entrez le prix du plat: "))
    personne = int (input("entrez le nombre de personne: "))
    total = prix * personne
    print(total)
except ValueError:
    print("Erreur! entrez un nombre")
except ZeroDivisionError:
    print("Erreur! division par zéro impossible")
    
# Partie 7 - API
import requests
requete = requests.get("https://api.agify.io?name=phanouel")
if requete.status_code == 200: 
    data = requete.json()
    if data.get('age') is None:
        print(f"le prénom {data['name']} n'est pas répertoriés dans cette API")
    else:
        print(f"Selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans")
else:
    print(f"erreur de connexion a l'API (code: {requete.status_code})")





