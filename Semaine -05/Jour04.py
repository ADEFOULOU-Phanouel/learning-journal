# Projet : Générateur de rapport
import random
noms = ["jean", "jacques", "anne", "fidèle", "eric"]
etudiants = []
for nom in noms:
    note=random.randint(0,20)
    age = random.randint(15,25)
    code_etudiant = random.randint(1000,9999)
    etudiants.append({"nom":nom, "note":note, "age":age, "code_étudiant":code_etudiant})
    print(etudiants)
for etudiant in etudiants:
    print(etudiant)
import math
somme = 0
moyenne = 0
for etudiant in etudiants:
    somme += etudiant['note']
    moyenne = somme / len(etudiants)
print(f"somme:{somme}")
print(f"moyenne: {moyenne}")
moyenne = round(moyenne, 2)
print(moyenne)

big = max(etudiants, key =lambda e:e['note'])
print(f"{big['nom']}:{big['note']}")
smole = min(etudiants, key =lambda e:e['note'])
print(f"{smole['nom']}:{smole['note']}")
for etudiant in etudiants:
    if etudiant['note']>10:
        print(f"{etudiant['nom']}:{etudiant['note']}-> Admis")
        
def mention(note):
    if note>=19:
        return("mention honorable")
    elif note >=18:
        return("mention excellente")
    elif note >=16:
        return("mention très bien")
    elif note >=14:
        return("mention bien")
    elif note >=12:
        return ("mention assez bien")
    elif note>=10:
        return("mention passable")
    else :
        return("mention insuffissant")
for etudiant in etudiants:
    m = mention(etudiant['note'])
    print(f"{etudiant['nom']}:{m}")
import datetime
jour = datetime.date.today()
print(f"Le rapport a été généré le {jour}")
h = datetime.datetime.now()
print(f"le rapport a été généré a {h.hour}:{h.minute}")

import json
import os
os.makedirs("semaine-05", exist_ok=True)

with open ("semaine-05/rapport.json","w") as f:
    json.dump(etudiants,f)
print("fichier sauvegardé !")
with open("semaine-05/rapport.txt","w") as f:
    f.write(f"{etudiants}\n")
    f.write(f"{moyenne}\n")
    f.write(f"{big} and {smole}\n")
    f.write(f"{jour} et {h}\n") 
print("fichier sauvegardé !") 
with open("semaine-05/rapport.txt","r") as f:
    for ligne in f:
        print(ligne.strip())  

    



