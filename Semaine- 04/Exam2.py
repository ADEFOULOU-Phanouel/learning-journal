# Partie 1__Variables, conditions et boucles
nom_entreprise = "EMES SARL"
année_création = 2021
nombre_employé = 5
print(f"l'entreprise {nom_entreprise} créer en {année_création} compte {nombre_employé} employées ")
if nombre_employé >= 50:
    print("Grande entreprise")
else:
    print("petite entreprise")
département = ["Littorale", "atlantique", "colline", "Zou", "borgou"]
i=0
for départements in département:
    i+=1
    print(f"{i}:{départements}")
    
# Partie 2__Fonctions
def creer_employe(nom, salaire, poste="stagiaire"):
    return {"nom":nom, "salaire":salaire, "poste":poste}
print(creer_employe("phanouel", 200.000))
def niveau(salaire):
    if salaire<200000:
        return("junior")
    elif salaire < 500000:
        return("senior")
    else:
        return("directeur")
print(niveau(2500000))    

def calculer_prime(salaire, taux=10):
    prime = (salaire * taux)/100
    return(prime)
print(calculer_prime(200000))
# partie 3__Listes des dictionnaires
employés=[
    creer_employe("phanouel",2000000,"ingénieure IA"),
    creer_employe("lisa",100000,"sécrétaire"),
    creer_employe("ella",20000),
    creer_employe("luc",1000000,"data scientist"),
    creer_employe("mael",100000),
]
print(employés)
for employé in employés:
    print(f"{employé}")
    
for employé in employés:
    m= niveau(employé['salaire'])
    print(f"{employé['nom']}:{m}") 
    
big = max(employés, key=lambda e:e['salaire'])
print(f"{big['nom']}:{big['salaire']}") 
somme=0
for employé in employés:
    somme+=employé['salaire']
print(somme)

# Partie 4__Fichiers
import json
employés=[
    creer_employe("phanouel",2000000,"ingénieure IA"),
    creer_employe("lisa",100000,"sécrétaire"),
    creer_employe("ella",20000),
    creer_employe("luc",1000000,"data scientist"),
    creer_employe("mael",100000),
]
with open("employés.json", "w") as f:
    json.dump(employés,f)
    print("fichier sauvegarder !")

with open("employés.json", "r") as f:
    contenu=json.load(f)
    print(contenu)
for ligne in contenu:
    print(ligne)
with open("nom.txt", "w") as f:
    f.write("nom : Phanouel \n"),
    f.write("nom : lisa\n"),
    f.write("nom : ella \n"),
    f.write("nom : luc \n"),
    f.write("nom : mael \n")
print("fichier sauvegarder !")
with open("nom.txt", "r") as f:
    data=f.read()
    print(data)
with open("nom.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
    
    


    