# Sujet : Système de gestion d'une université
# Partie 1 : Variables, conditions et boucles 
nom_universite = "Université d'Abomey Calavi"
annee_creation = 2000
nombre_etudiant = 20000 
print(f"L'{nom_universite} créer en {annee_creation} compte {nombre_etudiant} étudiant.")

if nombre_etudiant>500:
    print("Grande université")
else:
    print("Petite université")
somme = 0  
facultés = ["FLAAC", "FASH", "FASEG", "FAST", "FADESP"]
for faculté in facultés:
    somme += 1
    print(f"{somme +0}:{faculté}")
    
# Partie 2 : Fonctions
def calculer_mention(note):
    if note >= 18:
        return("mention excellente")
    elif note >=16:
        return("mention très bien")
    elif note>=14:
        return("mention bien")
    elif note >=12:
        return("mention assez bien")
    elif note >=10:
        return("mention passable")
    else:
        return("mention insuffisant")

print(calculer_mention(17)) 
print(calculer_mention(7))   

def est_admis(note):
    if note >=10:
        return True
    else:
        return False
print(est_admis(6))
print(est_admis(20))

def appliquer_bourse(salaire, taux=10):
    result = salaire * taux /100
    return result
print(appliquer_bourse(400000))
print(appliquer_bourse(20000)) 

# Partie 3 : POO
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self):
        print(f"je m'appelle {self.nom} et j'ai {self.age} ans")
        
class Etudiant(Personne):
    def __init__(self, nom, age, filiere, code):
        super().__init__(nom, age)
        self.filiere = filiere
        self.code = code
        self.moy = 0
        self.notes = []
    
    def ajouter_note(self,note):
        self.notes.append(note)
        print(f"notes ajoutées. notes:{self.notes}")
        
    def moyenne(self):
        self.moy = sum(self.notes) / len(self.notes) 
        return(f"{self.moy}")
    
    def mention(self):
        m = sum(self.notes) / len(self.notes)
        if self.moy >= 18:
            return("mention excellente")
        elif self.moy >=16:
            return("mention très bien")
        elif self.moy >=14:
            return("mention bien")
        elif self.moy >=12:
            return("mention assez bien")
        elif self.moy >=10:
            return("mention passable")
        else:
            return("mention insuffisant")
        
    def est_admis(self):
        if self.moy >=10:
            return True
        else:
            return False
    
    def __str__(self):
        return(f"{self.nom}: {self.filiere}")
        
class Professeur(Personne):
    def __init__(self, nom, age, matiere, salaire):
        super().__init__(nom, age)
        self.matiere = matiere
        self.salaire = salaire
        
    def enseigner(self):
        print(f"le professeur {self.nom} agée de {self.age} enseigne la matière {self.matiere} et gagne pour ca {self.salaire}")
        
    def calculer_prime(self,taux= 10):
        result = (self.salaire * taux)/ 100
        return (result)
    
class Universite:
    def __init__(self, nom, age, ):
        self.etudiant = []
        self.professeur = []
        
    def ajouter_etudiant(self, etudiant):
        self.etudiant.append(etudiant)
        print(f"Etudiant ajouter. Etudiant : {etudiant.nom}")
        
    def ajouter_professeur(self, professeur):
        self.professeur.append(professeur)
        print(f"Professeur ajouter. professeur : {self.professeur}")
        
    def afficher_raapport(self):
        print("---Etudiant---")
        for e in self.etudiant:
            print(f"{e.nom} : {e.moyenne()} : {e.mention()}")
        print("---professeur---")
        for p in self.professeur:
            print(f"{p.nom} : {p.salaire} : {p.calculer_prime()}")
            
    def moyenne_general(self):
        total = sum(e.moy for e in self.etudiant)
        return total / len(self.etudiant)

    def meilleur_etudiant(self):
        return max(self.etudiant, key=lambda e: e.moy)

e1 = Etudiant("Abel", 17, "Intélligence Artificielle", 111)
e2 = Etudiant("lisa", 18, "génie logicielle", 122)
e3 = Etudiant("Manel", 19, "sécurité informatique", 121)
e1.se_presenter()
e1.ajouter_note(15)
e1.ajouter_note(12)
e1.ajouter_note(13)
e1.moyenne()
print(e1.mention())
print(e1.est_admis())

e2.se_presenter()
e2.ajouter_note(18)
e2.ajouter_note(11)
e2.ajouter_note(19)
e2.moyenne()
print(e2.mention())
print(e2.est_admis())

e3.se_presenter()
e3.ajouter_note(9)
e3.ajouter_note(4)
e3.ajouter_note(10)
e3.moyenne()
print(e3.mention())
print(e3.est_admis())



p1 = Professeur("Ina", 30, "algorithmique", 2000000)
p2 = Professeur("gilles", 28, "Logique informatique", 3000000)

universite = Universite("Université générale", 20000)
e2.ajouter_note(18)
e2.ajouter_note(16)
e2.ajouter_note(19)
e2.moyenne()

e3.ajouter_note(8)
e3.ajouter_note(9)
e3.ajouter_note(7)
e3.moyenne()

universite.ajouter_etudiant(e1)
universite.ajouter_etudiant(e2)
universite.ajouter_etudiant(e3)
universite.ajouter_professeur(p1)
universite.ajouter_professeur(p2)

universite.afficher_raapport()
print(f"Moyenne générale : {universite.moyenne_general():.2f}")
print(f"Meilleur étudiant : {universite.meilleur_etudiant()}")

# Partie 4: Listes des dictionnaires
def creer_cours(nom, credits, obligatoire=True):
    return {"nom":nom, "credits":credits, "obligatoire": obligatoire}

cours = [
    creer_cours("Algèbre linéaire", 5, True), 
    creer_cours("anglais technique", 2, False),
    creer_cours("logique informatique", 5, True),
    creer_cours("infographie", 2, False)
]

for cour in cours:
    print(cour)

for cour in cours:
    if cour['obligatoire'] == True:
        print(cour)
    else: 
        print("pas forcément")
        
big= max( cours, key= lambda  e:e['credits'])
print(f"{big['nom']}:{big['credits']}")

somme = 0
for cour in cours:
    somme += cour['credits']
print(somme)

# Partie 5: Fichiers JSON et TXT
import json
etudiants=[
    {"nom":"max","age":15,"note":13},
    {"nom":"elene","age":16,"note":7},
    {"nom":"david","age":14,"note":18},
    {"nom":"rahab","age":14,"note":8},
    {"nom":"anabelle","age":15,"note":15}
]
with open ("etudiants.json", "w") as f:
    json.dump(etudiants, f)
    print("fichier sauvegarder !")
with open ("etudiants.json", "r") as f:
    data = json.load(f)
    for ligne in data :
        print(ligne) 
        
with open ("nom.txt", "w") as f:
    for etudiant in etudiants:
        f.write(f"{etudiant['nom']}\n")
        print("nom sauvegarder !")
        
with open ("nom.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
        
# Partie 6: Modules
import random
numero_etudiant = random.randint(10000,99999)
print(numero_etudiant)
import datetime
jour = datetime .date.today()
print(f" nous sommes le {jour}")
h = datetime.datetime.now()
print(f"Il est {h.hour}:{h.minute}")
jour_retants = datetime.date(jour.year, 12, 31)
f = (jour_retants - jour).days
print(f"Il reste exactement {f} jour avant le 31 décembre")
import math
print(math.sqrt(numero_etudiant))
print(math.ceil(numero_etudiant))
import os
os.makedirs("rapports_universite/", exist_ok=True)
print("dossier crer !")

# Partie 7: Gestion des erreurs
try:
    note = int(input("entrez une note: "))
    if note > 20:
        print("note impossible ! entre 0 et 20")
    else:
        print(f"{calculer_mention(note)}")
except ValueError:
    print("impossible! entrez un nombre")
# Partie 8: API
import requests
import requests
requete = requests.get("https://api.agify.io?name=phanouel")
if requete.status_code == 200: 
    data = requete.json()
    if data.get('age') is None:
        print(f"le prénom {data['name']} n'est pas répertoriés dans cette API")
    else:
        print(f"Selon cette API,le prénom {data['name']} a en moyenne {data['age']} ans")
else:
    print(f"erreur de connexion a l'API (code: {requete.status_code})")








        

        
       






        
        
            
       
         
        
    
            
        
    
    
        
        
    

    

    
 


    

    
    