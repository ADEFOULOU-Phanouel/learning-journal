import os
# connaitre le dossier actuel
print(os.getcwd()) # Afficher le chemin actuel

# Lister les fichiers du dossier actuel
fichiers = os.listdir(".")
print(fichiers)

# Créer un nouveau dossier
os.makedirs("mon_dossier", exist_ok=True)
print("dosssier créer !")

# Vérifier si un fichier existe
print(os.path.exists("notes.txt")) # True ou false
print(os.path.exists("inexistant.txt")) # False

# Connaitre la taille d'un fichier
if os.path.exists("notes.txt"):
    taille = os.path.getsize ("notes.txt")
    print(f"taille : {taille} octets")
    
# Renommer un fichier
if os.path.exists("notes.txt"):
    os.rename("notes.txt", "notes_backup.txt")
    print("fichier renommée !")
    
# Mini-défi
print(os.getcwd())  
os.makedirs("backup", exist_ok=True)
print("dossier créer !")
with open ("backup/données.txt", "w") as f:
    f.write("salut !\n")
    f.write("je m'appelle ADEFOULOU Phanouel.\n")
    f.write("J'aime python.\n")
print("fichier créer !")

print(os.path.exists("backup/données.txt"))

if os.path.exists("backup/données.txt"):
    taill = os.path.getsize("backup/données.txt")
    print(f"taille :{taill} octets")
    

    # Partie 1 — Variables, conditions, boucles (10 points)
   # Création des variables : nom du magasin, année de création, nombre de clients
nom_magasin = "ADEF Sarl"
année_création = 2026
nombre_client = 500   

# Affiche : "Le magasin [nom] compte [X] clients depuis [année]"
print(f"Le magasin {nom_magasin} compte {nombre_client} clients depuis {année_création}")

# Si plus de 200 clients → "Grand magasin", sinon → "Petit magasin"
if nombre_client >=200:
    print(f"{nom_magasin}:grand magasin")
else:
        print(f"{nom_magasin}:petit magasin")


# Crée une liste de 5 catégories de produits et affiche chacune avec son numéro
catégories = ["Javel", "riz", "biscuit", "farine de blée", "croquette"]
i=0
for catégorie in catégories:
    i+=1
    print(f"{i}:{catégorie}")

#Partie 2 — Fonctions (12 points)

# Crée ces fonctions, toutes avec return :
# creer_produit(nom, prix, stock=0) → retourne un dictionnaire
def creer_produit(nom, prix, stock=0):
    return({"nom":nom, "prix":prix,"stock":stock})
print(creer_produit("riz", 2000))

# est_disponible(stock) → retourne True si stock > 0, sinon False
def est_disponible(stock):
    if stock > 0:
        return(True)
    else:
        return(False)
print(est_disponible(10))

# appliquer_remise(prix, remise=5) → retourne le prix après remise en %
def appliquer_remise(prix, remise=5):
    remix = prix - (prix * remise) / 100
    return(remix)
print(appliquer_remise(2000))

# mention_stock(stock) → retourne "rupture" si stock == 0, "faible" si < 5, "bon" sinon
def mention_stock(stock):
    if stock==0:
        return("rupture")
    elif stock < 5:
        return("faible")
    else:
        return("bon")
print(mention_stock(20))

# Partie 3 — Listes de dictionnaires (12 points)

# Crée une liste de 6 produits avec creer_produit
produits = [
    creer_produit("riz",10000,20),
    creer_produit("javel",2000,500),
    creer_produit("bouteille d'eau",500,200),
    creer_produit("croquette",3000,100),
    creer_produit("farine de blée",2000),
    creer_produit("biscuits",20000,500)
]
# Affiche tous les produits
for produit in produits:
    print(produit)
# Affiche seulement les produits disponibles
somme = 0
for produit in produits:
    somme += produit["prix"] * produit["stock"]
print(f"Valeur totale du stock : {somme}")


# Affiche le statut de stock de chaque produit (mention_stock)
for produit in produits:
    t=mention_stock(produit['stock'])
    print(f"{produit['nom']}:{t}")

# Affiche le prix après 10% de remise pour chaque produit
for produit in produits:
    u = appliquer_remise(produit['prix'])
    print(f"{produit['nom']} : {u}")

# Affiche le produit le plus cher et le moins cher
big= max(produits ,key=lambda e:e['prix'])
print(f"{big['nom']}:{big['prix']}")

smole = min(produits, key=lambda e:e['prix'])
print(f"{smole['nom']}:{smole['prix']}")

# Calcule et affiche la valeur totale du stock (somme des prix)
somme=0
for produit in produits:
    somme+=produit["prix"]
moy= somme/len(produits)
print(somme)
print(moy)


# Partie 4 — Fichiers (10 points)
import json
# Sauvegarde la liste des produits dans produits.json
with open("produits.json", "w") as f:
    json.dump(produits, f)
    print("fichier sauvegarder !")
    
# Relis le fichier et affiche chaque produit
with open ("produits.json", "r") as f:
    contenu=json.load(f)
    print(contenu)
for ligne in contenu:
    print(ligne)

# Sauvegarde uniquement les noms des produits dans noms_produits.txt
with open("nom_produits.txt", "w") as f:
    for produit in produits:
        f.write(f"{produit['nom']}\n")
    print("fichier sauvegarder !")    

# Relis ce fichier et affiche chaque nom
with open("nom_produits.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())

# Partie 5 — Gestion des erreurs (8 points)

# Demande à l'utilisateur un prix (nombre) et une quantité (nombre)
try:
    prix = int(input("entrez un prix: "))
    quantité = int(input("entrez une quantité: "))
    result = prix * quantité
    print(result)
except ZeroDivisionError:
    print("erreur ! Le nombre ne peut etre divisé par zéro")
except ValueError:
    print("erreur ! entrez un nombre")

#Partie 6 — Modules (8 points)
import random
import datetime
import os
# Utilise random pour générer un code client aléatoire entre 1000 et 9999
f=random.randint(1000,9999)
print(f)

# Utilise datetime pour afficher la date du jour et calculer combien de jours restent avant le 31 décembre de cette année
jour = datetime.date.today()
print(f"la date d'aujourd'hui est : {jour}")
h= datetime.datetime.now()
print(f"il est actuellement {h.hour}:{h.minute}")
fin_annee= datetime.date(jour.year,12,31)
jour_restant= (fin_annee-jour).days
print(f"le nombre de jour restant avant noel est: {jour_restant} jour")

# Utilise os pour créer un dossier sauvegardes/ s'il n'existe pas, et vérifier s'il existe bien
print(os.path.exists("sauvegardes/"))# true or false
os.makedirs("sauvegardes/", exist_ok=True)
print("dossier créer !")
print(os.path.exists("sauvegardes/"))# true or false

