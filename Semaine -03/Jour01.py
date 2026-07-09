# Fonction avec print(Mauvaise pratique)
def mention_print(note):
    if note >= 16:
        print("excellent")
    elif note >=10:
        print("passable")
    else:
        print("insuffisant")
        
# Fonction avec return (Bonne pratique)
def mention_return(note):
    if note >= 16:
        return("excellent")
    elif note >=10:
        return("passable")
    else:
        return("insuffisant")
    # Test des deux
mention_print(15)
resultat = mention_print(15)
print(f"Mention : {resultat}")

# Pourquoi return est meilleur?: Tu peux réutiliser la valeur.
eleves =[
    {"nom":"Phanouel", "note":15},
    {"nom":"Alice", "note": 8}
]
for eleve in eleves:
    m= mention_return(eleve['note'])
    print(f"{eleve['nom']} : {m}") 
# Mini-défi
eleves = [
     {"nom":"Phanouel", "note":18},
    {"nom":"Alice", "note": 9},
    {"nom":"Jean", "note":14},
    {"nom":"Sarah", "note": 16}
 ]
# Partie 1
def mention(note):
    if note>=16:
        return("Excellent")
    elif note >= 14:
        return("très bien ")
    elif note >= 10:
        return("passable")
    else:
        return("insuffissant")
# Partie 2
for eleve in eleves:
    m= mention(eleve['note'])
    print(f"{eleve["nom"]}: {m}")    
# partie 3
produits=[
    {"nom": "chaussure", "prix":15000},
    {"nom": "chemise", "prix":8000},
    {"nom": "pantalon", "prix":12000},
]
def calculer_prix(prix, reduction):
    reduct = prix-(prix*(reduction/100))
    return reduct
print(calculer_prix(15000,15))
print(calculer_prix(8000,15))
print(calculer_prix(12000,15))
#Partie 4
# 1- Fonction qui retourne True/False en fonction de l'age
def est_majeur(age):
    if age>=18:
        return("True")
    else:
        return("False")
print(est_majeur(15))
print(est_majeur(25))
# 2- Fonction qui retourne le statut en fonction de l'age
def categorie(age):
    if age>=18:
        return("Adulte")
    elif age>=12:
        return("Adolescent")
    else :
        return("enfant")
print(categorie(8))
print(categorie(16))
print(categorie(27))
# 4- fonction sur une liste de dictionnaire
personnes = [
    {"nom":"phanouel", "age":19},
    {"nom":"Alice", "age":15},
    {"nom":"Marc", "age":8},
    {"nom":"Sarah", "age":22}
]
for personne in personnes:
    cat= categorie(personne["age"])
    maj= est_majeur(personne['age'])
    print(f"{personne['nom']}:{cat} et {maj}")

    