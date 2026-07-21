import json
# Sauvegarder un dictionnaire dans un fichier json
etudiant={
    "nom":"Phanouel",
    "age":19,
    "notes": [12,14,16]
}
with open("etudiant.json", "w") as f:
    json.dump(etudiant, f)
print("fichier JSON créer")
# Lire un fichier json
with open("etudiant.json", "r") as f:
    data= json.load(f)
print(data)
print(f"Nom : {data['nom']}")
print(f"Moyenne : {sum(data['notes'])}")

# Sauvegarder une liste de dictionnaire
eleves = [
    {"nom":"Phanouel", "note":15},
    {"nom":"Alice", "note":12},
    {"nom":"Marc", "note":18},

]
with open("eleves.json", "w") as f:
    json.dump(eleves, f)
# Relire et afficher
with open("eleves.json", 'r') as f:
    data= json.load(f)
    
for eleve in data:
    print(f"{eleve["nom"]} : {eleve['note']}") 
# Mini-défi
produits=[
    {"nom":"Riz","prix":2000},
    {"nom":"javel","prix":1000},
    {"nom":"Chemise","prix":1500},
    {"nom":"Farine","prix":6000},
]
with open("produits.json", "w") as f:
    json.dump(produits, f)
print("fichier JSON créer !")
with open("produits.json", "r") as f:
    data = json.load(f)
for produit in data:
    print(f"{produit['nom']}:{produit['prix']}")
for produit in data: 
    if produit['prix']<5000:
        print(produit['nom'])
#   Partie 2
employes=[
    {"nom":"luc","salaire":200000, "département":"finance"},
    {"nom":"lise","salaire":100000, "département":"marketing"},
    {"nom":"Jean","salaire":150000, "département":"juridique"},
    {"nom":"marc","salaire":600000, "département":"informatique"},
]
with open("employes.json", "w") as f:
    json.dump(employes, f)
print("fichier JSON créer !")
with open ("employes.json", "r") as f:
    data=json.load(f)
for employee in data:
    print(f"{employee['nom']}-{employee['salaire']}-{employee['département']}")
    print(employee)
for employee in data:
    if employee['salaire']>200000:
        print(employee['nom'])
somme=0 
moy=0    
for employee in data:
    somme+=employee['salaire']
moy=somme / len(employes)
print(somme)
print(moy)
 