# Partie 1 - Donnée de départ
nom_ecole = "Harmonia"
annee_fondation = 2010
nombre_eleves = 150
print(f"l'école {nom_ecole} a été fondée en {annee_fondation} et compte {nombre_eleves} élèves")

nombre_annee = 2026 - 2010
print(f"{nombre_annee}")

nom = input("entrez votre nom ? : ")
print(f"Bienvenu {nom} a harmonia !")

# Partie 2 - Fonctions
def mention(note):
    if note >= 16:
        return ("Excellent !")
    elif note >= 12:
        return ("Bien !")
    else:
        return ("insuffisant !")
eleves=[
    {"nom":"max","note":13},
    {"nom":"elene","note":7},
    {"nom":"david","note":18},
    {"nom":"rahab","note":8},
    {"nom":"anabelle","note":15}
]
for eleve in eleves:
    m =mention(eleve['note'])
    print(f"{eleve['nom']}: {m}")

# Partie 3 -Fichier et erreur
import json
with open("eleves.json", "w") as f:
    json.dump(eleves, f)
print(f" Fichier sauvegarder !")
try:
    with open("eleves.json", "r") as f:
        data = json.load(f)
        for ligne in data:
            print(ligne)
except FileNotFoundError:
    print("Erreur de fichier")
    
# Partie 4 - Modules
import datetime
j = datetime.date.today()
print(f"Nous sommes le {j}")

import random
for eleve in eleves:
    e = random.choice(eleves)
print(f"{eleve['nom']}: {e}")

# Partie 5 - POO
class Eleve:
    def __init__(self,nom, instrument, note):
        self.nom = nom
        self.instrument = instrument
        self.note = note
    def afficher(self):
        print(f"{self.nom} utilise {self.instrument} comme instrument pour finalement obtenir une note de {self.note}")

        

class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.eleve = []
    def ajouter_eleve(self,eleve):
        self.eleve.append(eleve)
        print(f'eleve ajoutée : {eleve.nom}')
        
    def moyenne_general(self):
        total = sum(e.note for e in self.eleve)
        return total / len(self.eleve)

    
    def afficher_rapport(self):
        for e in self.eleve:
            print(f"{e.nom} : {e.note} ")
            
e1 = Eleve("emeraude", "regle", 13)
e2 = Eleve("franck", "ine", 15)
e3 = Eleve("jilles", "mot", 2)
e4 = Eleve("jacques", "RAS", 19)
e1.afficher()
e3.afficher()
e2.afficher()
e4.afficher()

# Partie 6 - Structures avancées

nom_eleve = [(p['nom'], p['note']) for p in eleves if p['note']>=12]
print(nom_eleve)
resultat = list( filter(lambda e:e['note'] < 12, eleves))
print([e['nom'] for e in resultat])











    

    


    

