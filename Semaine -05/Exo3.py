# Partie1- Variable, condition et boucles
nom_pharmacie = "La rose"
annee_ouverture = 2021
nombre_medicament = 800
print(f"la pharmacie {nom_pharmacie} ouverte en {annee_ouverture} a {nombre_medicament} medicaments")

if nombre_medicament>100:
    print("grande pharmacie")
else:
    print("petite pharmacie")
    
medicaments = ["paracétamol", "amoxiciline","ibuprofene","doliprane", "ventoline"]
somme = 0
for medicament in medicaments:
    somme+=1
    print(f"{somme}:{medicament}")
# partie2: Fonctions
def crer_medicament(nom, prix, stock=0, ordonnance=False):
    return {"nom":nom,"prix":prix, "stock":stock, "ordonnance":ordonnance}
print(crer_medicament("stick",200, 2))

def est_disponible(stock):
    if stock>0:
        return True
    else:
        return False
print(est_disponible(56))

def calculer_prix(prix, remise = 5):
    result = prix- (prix * remise)/100
    return result
print(calculer_prix(20000))

def mention_stock(stock):
    if stock<=0:
        return("rupture")
    elif stock<5:
        return("faible")
    else:
        return("bon")
print(mention_stock(3))

# partie 3- Listes de dictionnaires

medicaments = [
    crer_medicament("paracétamol",500,500,True),
    crer_medicament("amoxiciline",1000,200,True),
    crer_medicament("ibuprofene",1500,0,True),
    crer_medicament("doliprane",2000,700),
    crer_medicament("ventoline",2500,),
    crer_medicament("metformine",3000,1000,)
]
for medicament in medicaments:
    print(medicament)
for medicament in medicaments:
    m = est_disponible(medicament['stock'])
    print(f"{medicament['nom']}:{m}")
    
big = max(medicaments, key=lambda e:e['stock'])
print(f"{big['nom']}:{big['prix']}")

somme=0
for medicament in medicaments:
    somme+=medicament['stock']
print(f"somme:{somme}")
import json
# partie4: Fichiers
medicaments = [
    crer_medicament("paracétamol",500,500,True),
    crer_medicament("amoxiciline",1000,200,True),
    crer_medicament("ibuprofene",1500,0,True),
    crer_medicament("doliprane",2000,700),
    crer_medicament("ventoline",2500,),
    crer_medicament("metformine",3000,1000,)
]

with open("medicaments.json", "w")  as f:
    json.dump(medicaments,f)
print("fichier sauvegarder !")

with open("medicaments.json", "r") as f:
    contenu=json.load(f)
print(contenu)
for ligne in contenu:
    print(ligne)
    
with open("medicaments.txt", "w") as f:
    for medicament in medicaments:
        f.write(f"{medicament['nom']}\n")
    print("ficher sauvegarder!")
with open("medicaments.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
# partie 4 - modules
import random
import os
numéro = random.randint(10000, 99999)
print(numéro)
import datetime
jour= datetime.date.today()
print(f"Nous sommes le {jour}") 
h = datetime.datetime.now()
print(f"il est {h.hour}:{h.minute}") 

fin_annee=datetime.date(jour.year,12,31)
jour_restant = (fin_annee - jour).days
print(f" il reste exactement {jour_restant} jour")
os.makedirs("rapport_pharmacie/", exist_ok=True)
print("dossier crer !")

# partie 6- Gestion des erreurs
try:
    prix_medicament = int(input("entrez le prix: "))
    quantité = int(input("entrez  la quantité du médicament: "))
    total = prix_medicament/quantité
    print(total)
except ValueError:
    print("Erreur !entrez un nombre")
except ZeroDivisionError:
    print("Erreur! Division par zero impossible")

# Partie 7 - API
import requests
requete = requests.get("https://api.agify.io?name=phanouel")
data = requete.json()
if 'error' in data:
    print(f"Erreur API : {data['error']}") 
else:
    print(f"selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans")
    
import requests

requete = requests.get("https://api.agify.io?name=phanouel")

if requete.status_code == 200:
    data = requete.json()
    # Si le prénom n'est pas trouvé, l'API renvoie age: null (qui devient None en Python)
    if data.get('age') is None:
        print(f"Le prénom {data['name']} n'est pas répertorié dans l'API.")
    else:
        print(f"Selon cette API, le prénom {data['name']} a en moyenne {data['age']} ans")
else:
    print(f"Erreur de connexion à l'API (Code : {requete.status_code})")


    
  



        
    
    


  


