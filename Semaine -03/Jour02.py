# Fonction avec valeur par défaut
def calculer_prix(prix, reduction=10):
    return(prix - (prix*reduction/100))

# Sans préciser la réduction, utiliser 10% par défaut
print(calculer_prix(1000))
# En précisant la réduction, utiliser 20%
print(calculer_prix(1000, 20))

# Fonction avec plusieurs valeur par défaut
def creer_eleve(nom, note=0, ville='cotonou'):
    return{"nom":nom,"note":note,"ville":ville}
e1= creer_eleve("phanouel",15)
e2= creer_eleve("Alice")
e3= creer_eleve("marc",12,"parakou")
print(e1)
print(e2)
print(e3)   
# Mini-défi
def presentation(nom, age, pays="Benin"):
    return{"nom":nom,"age":age,"pays":pays}
e=presentation("Phanouel" , 19)
f=presentation("Alice", 15, "France")
print(f"je m'appelle {e['nom']}, j'ai {e['age']} ans et je viens du {e['pays']} ")
print(f"je m'appelle {f['nom']}, j'ai {f['age']} ans et je viens du {f['pays']} ")
# Partie 2
def creer_produit(nom, prix, categorie="alimentaire"):
    return {"nom":nom, "prix":prix, "categorie":categorie}
print(creer_produit("riz",1000))
produits= [
    creer_produit("Riz", 2000),
    creer_produit("Javel", 1500,"Menager"),
    creer_produit("table",5000,"Mobilier")
]
print(produits)

# partie 3
def creer_etudiant(nom, note, ville="cotonou"):
    return {"nom":nom, "note":note, "ville":ville}

etudiants=[
    creer_etudiant("hans", 19,"Abomey calavi"),
    creer_etudiant("Alice", 15),
    creer_etudiant("pierick", 12,"Abomey calavi"),
    creer_etudiant("Sarah", 9,),
    creer_etudiant("sam", 5),
]
print(etudiants)

def mention(note):
    if note>=16:
        return("excellente")
    elif note>=14:
        return ("bien")
    elif note>=12:
        return("passable")
    else:
        return("insuffissant")
for etudiant in etudiants:
    m = mention(etudiant['note'])
    print(f"{etudiant["nom"]}, {etudiant["ville"]},{m}")
    
    