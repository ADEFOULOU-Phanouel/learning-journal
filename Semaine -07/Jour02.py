# Méthode classique (longue)
# Syntaxe de base
carres = []
for i in range(1, 6): 
    carres.append(i ** 2)
    
# List comprehension (courte)
carres = [i ** 2 for i in range(1, 6)]
print(carres)

# Avec une condition(if)
notes = [12, 8, 15, 6, 18, 10, 14]

# Seulement les notes >=10
admis = [n for n in notes if n>= 10]
print( admis)

# # Avec transformation
prenoms = ["richard", "Phanouel", "alice"]
# Metre en majuscule
prenom_maj = [p.upper() for p in prenoms]
print(prenom_maj)
# Combinaison transformation + condition
notes = [12, 8, 15, 6, 18, 10, 14]
# Doublage des notes < 10 uniquement
rattrapages = [n * 2 for n in notes if n < 10]
print(rattrapages)

# Mini-défi
produits = [
    {"nom": "stylo", "prix": 500},
    {"nom": "cahier", "prix": 1500},
    {"nom": "sac", "prix": 8000},
    {"nom": "règle", "prix": 300},
    {"nom": "calculatrice", "prix": 5000},
]
# List comprehension des noms de tout les produits
nom = [i['nom']for i in produits]
print(nom)
# List comprehension des prix supérieure a 1000
prix = [i['prix'] for i in produits if i['prix']>1000]
print(prix)
nom_prix = [(p['nom'], p['prix']) for p in produits if p['prix']>1000]
print(nom_prix)






