# partie 1 : Fichier (json et txt)
import json
inventaires = [
    {"nom":"riz", "prix":2000,"stock":50},
    {"nom":"javel", "prix":1000,"stock":0},
    {"nom":"yaourt", "prix":500,"stock":300},
    {"nom":"clou", "prix":3000,"stock":500},
]
with open("inventaires.json", "w") as f:
    json.dump(inventaires, f)
print(" fichier json enrégistrer !")
with open("inventaire.json", "r") as f:
    contenu = json.load(f)
for ligne in contenu:
    print(ligne)
with open("noms.txt", "w") as f:
    for inventaire in inventaires:
        f.write(f"{inventaire['nom']}\n")
    print("fichier créer !")
with open("noms.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
        
# Partie 2: Fonctions
def creer_produits(nom , prix, stock=0):
    return {"nom":nom, "prix":prix, "stock":stock}
def est_disponible(stock):
    if stock > 0:
        return(True)
    else:
        return(False)
def appliquer_remise(prix, remise=10):
    app = prix - (prix * remise)/100
    return(app)

    # partie 3: Listes de dictionnaires
produits = [
 creer_produits("riz",2000),
 creer_produits("Ordinateurs",80000,800),
creer_produits("chips",2000, 300),
 creer_produits("pneu",7000, 10),
creer_produits("farine",10000)
]
for produit in produits:
    print(f"produit:{produit}")

for produit in produits:
    m = est_disponible(produit['stock'])
    print(f"{produit['nom']} : {m}")
    big = max(produits, key=lambda e:e['prix'])
print(f"{big['nom']}:{big['prix']}")
somme = 0
for produit in produits:
    somme += produit['prix']
    print(f"valeur total du stock:{somme}")

# partie 4: Module math, random et datetime
import math
import random
import datetime
code = random.randint(1000,9999)
print(f"code:{code}")

date = datetime.date.today()
print(f"nous sommes le : {date}")
h = datetime.datetime.now()
print(f"il est {h.hour}:{h.minute}")

fin_année = datetime.date(date.year,12,31)
jour_restant = (fin_année - date).days
print(f"le nombre de jour restant est de {jour_restant} jours.")
print(f"la racine carrée du code de commande est: {math.sqrt(code)}")

# partie 5: API avec request
import requests
import json
import math
requete = requests.get("https://api.agify.io?name=phanouel")
        
data = requete.json()
if 'error' in data:
    print(f"Erreur API : {data['error']}") 
else:
    print(f"selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans")
# Partie6: Gestion des erreurs
try:
    prix = int(input("entrez le prix: "))
    quantité = int(input("entrez la quantité: "))
    total = prix * quantité  
    print(total)
except ValueError:
    print("Erreur ! entrez un nombre")
except ZeroDivisionError:
    print("Erreur! division impossible") 
# Partie 7: Module OS
import os
print(os.getcwd())
os.makedirs("sauvegardes/",exist_ok = True)
print("dossier créer !")
print(os.path.exists("sauvegardes/"))




