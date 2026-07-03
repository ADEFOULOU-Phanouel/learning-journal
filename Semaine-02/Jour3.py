"""
 # Listes de dictionnaires
etudiants=[
    {"nom":"Phanouel", "moyenne":14},
    {"nom":"Alice", "moyenne":16},
    {"nom":"Sarah", "moyenne":16},
    {"nom":"Marc", "moyenne":9}
]
# Afficher tout les étudiants
for etudiant in etudiants:
    print(f"{etudiant['nom']} : {etudiant['moyenne']}/20")

# Afficher seulement les admis
print("Admis")
for etudiant in etudiants:
    if etudiants['moyenne']>=10:
        print(etudiants['nom'])
        
# Calculer la moyenne générale
somme = 0
for etudiant in etudiants:
    somme+= etudiant["moyenne"]

moyenne_generale = somme / len(etudiants) 
print(f"Moyenne générale : {moyenne_generale}/20")


# Mini-défi
# Créer listes de dictionnaires des produits
Produits=[
    {"nom":"Javel","prix":15000},
    {"nom":"huile", "prix":2000},
    {"nom":"savon", "prix":1000},
    {"nom":"céréale", "prix":25000}
] 
# Afficher tout les éléments
for Produit in Produits:
    print(f"{Produit["nom"]}: {Produit["prix"]}")
# Afficher les produits dont le prix est inférieure a 5000
for Produit in Produits:
    if Produit['prix']<=5000:
        print(f"{Produit['nom']}")
# Afficher la somme des prix
somme=0
for Produit in Produits:
    somme+=Produit['prix']
print(f"somme:", somme) 

# Exo 2
eleves=[
    {"nom":"max", "note":9},
    {"nom": "ella", "note":5},
    {"nom": "john", "note":16},
    {"nom": "myriam", "note":18},
    {"nom": "jules", "note":14}
]
for eleve in eleves:
    print(f"{eleve['nom']} : {eleve['note']}")
    
print("eleves admis")
for eleve in eleves:
    if eleve['note']>=10:
        print(eleve["nom"])
somme=0
for eleve in eleves:
    somme+= eleve['note']
moy= somme/ len(eleves)
print("somme:", somme)
print("moy:",moy) 

meilleur = max(eleves, key=lambda e: e['note'])
print(f" {meilleur['nom']} : {meilleur['note']}")
""" 
# Exo 3
villes = [
    {"nom":"Calavi", "population":200000},
    {"nom":"Cotonou", "population":700000},
    {"nom":"Parakou", "population":1000000},
    {"nom":"porto-novo", "population":1500000}
 ]
for ville in villes:
    print(f"{ville['nom']}: {ville['population']}")
    
for ville in villes: 
    if ville["population"]>=500000:
        print(ville["nom"])
        
big = max(villes, key=lambda e:e['population'])
print(f"{big['nom']}: ",big['population'])

        




 