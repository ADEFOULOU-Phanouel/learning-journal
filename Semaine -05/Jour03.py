import requests

# Faire une requete sur une API publique gratuite
reponse = requests.get("https://api.agify.io?name=phanouel")

# Vérifier que la requete a réussi (code 200 = Succès)
print(reponse.status_code)

# Récupéré les données en format JSON
data = reponse.json()
print(data)
if 'error' in data:
    print(f"Erreur API : {data['error']}")
else:
    print(f"selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans") 



# Mini - défi
# pip install requests
import requests
req = requests.get("https://api.genderize.io?name=marc")
print(req.status_code)
data2 = req.json()
print(data2)
if 'error' in data2:
    print(f"Erreur API: {data['error']}")
else:
    print(f"selon cette API, le prénom {data2['name']} est probablement {data2['gender']} avec une probabilité de {data2['probability']}")

# Mini-défi 2
#Importe requests
import requests
# Fait une requête sur l'API publique https://api.nationalize.io?name= + un prénom de ton choix
avis= requests.get("https://api.nationalize.io?name=Phanouel")
# Récupère les données en JSON avec .json()
données = avis.json()
print(données)
# Affiche le prénom et la liste des pays probables (country) avec leur code pays (country_id) et leur probabilité (probability)
for pays in données['country']:
    if 'error' in data2:
        print(f"Erreur API: {data['error']}")
    else:
        print(f"selon cette API, le prénom {données['name']} pourrait venir de {pays['country_id']} avec une probabilité de {pays['probability']}")







