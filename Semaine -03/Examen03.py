# Parie 1: Gestion d'une bibliothèque
nom_bibliotheque= "Bénin excellence"
Anneee_creation= 2010
Nombres_livres=2000
print(f"la bibliothèque {nom_bibliotheque} a {Nombres_livres} livres depuis {Anneee_creation} ")
if Nombres_livres>=1000:
    print("Grande bibliothèque")
else:
    print("petite bibliothèque")
genres=["Policier", "Roman", "féérique", "science-fiction", "comédie"]
i=0
for genre in genres:
    i+=1
    print(f"{i}-{genre}")
    
# Partie 2:  Fonctions
def est_disponible(stocks):
    if stocks>0:
        return(True)
    else:
        return(False)
print(est_disponible(15))

def categorie_livre(pages):
    if pages<100:
        return("court")
    elif pages<300:
        return("moyen")
    else:
        return("long")
print(categorie_livre(1000))
def calculer_prix(prix, remise):
    reduct= prix - ((prix * remise)/100)
    return(reduct)
print(calculer_prix(100000, 20))
# Partie 3: Liste de dictionnaire
Livres=[
    {"titre":"Sous l'orage","auteur":"SEIDOU Badian","pages":400, "prix":2500,"stock":28},
    {"titre":"un piège sans fin","auteur":"Olympe belim Quenum","pages":600, "prix":3000,"stock":45},
    {"titre":"Sans tam-tam","auteur":"Henri LOPEZ","pages":90, "prix":4000,"stock":0},
    {"titre":"Les frasques d'ébinto","auteur":"Gérard martin","pages":200, "prix":2500,"stock":0},
    {"titre":"Tombeau du désert","auteur":"Richard Franck","pages":1000, "prix":2500,"stock":100},

]
for livre in Livres:
    print(livre)
for livre in Livres:
    m=est_disponible(livre['stock'])
    print(f"{livre['titre']}:{m}")
for livre in Livres:
    n= categorie_livre(livre["pages"])
    print(f"{livre["titre"]}:{n}")
for livre in Livres:
    p= calculer_prix(livre['prix'],10)
    print(f"{livre['titre']}:{p}")
big= max(Livres, key=lambda e:e['prix'])
print(f"{big['titre']}:{big['prix']}")
    

    

    
      
     