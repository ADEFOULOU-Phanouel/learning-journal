import requests

# Faire une requete sur une API publique gratuite
reponse = requests.get("https://api.agify.io?name=phanouel")

# Vérifier que la requete a réussi (code 200 = Succès)
print(reponse.status_code)

# Récupéré les données en format JSON
data = reponse.json()
print(data)

print(f"selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans") 


# Mini - défi
# pip install requests
req = requests.get("https://api.genderize.io?name=phanouel")
print(req.status_code)


# Exo
import random
import datetime
import json
commande = random.randint(1000,9999)
print(commande)
date = datetime.date.today()
print(f"Aujourd'ui, nous somme le {date}")
h= datetime.datetime.now()
print(f"Il est actuellement {h.hour} heure:{h.minute} minutes:{h.second} secondes")
m= datetime.date(date.year,12,31)
jour_restant = (m-date).days
print(f"Le nombre de jour restant avant la fin de cette année est de {jour_restant}  jour")

try:
    prix = int(input("entrez un prix: "))
    quantité = int(input("entrez une quantité: "))
    result = prix * quantité
    print(quantité)
except ZeroDivisionError:
    print("Erreur ! division impossible")
except ValueError:
    print("Erreur ! entrez u nombre entier")
