# Examen
#Partie1: Fichier txt
with open("courses.txt", "w") as f:
    f.write("chips : 25 \n"),
    f.write("farine de blée : 5 \n"),
    f.write("croquette pour chien: 40\n"),
    f.write("cloue : 30 \n"),
    f.write("machine a lavé : 02 \n")
print("fichier txt créer !")

with open("courses.txt", "r") as f:
    contenu=f.read()
    print(contenu)
with open("courses.txt", 'r') as f:
    for ligne in f:
        print(ligne.strip())
        
with open("courses.txt","a") as f:
    f.write("biscuit : 20\n"),
    f.write("lessive : 50\n")
print("biscuit et lessive ajouter !")
with open("courses.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())    
# Partie 2: Fichier JSON
import json

magasin =[
    {"nom":"chips","prix":2000,"stock":25},
    {"nom":"farine","prix":6000,"stock":5},
    {"nom":"croquette","prix":20000,"stock":0},
    {"nom":"cloue","prix":3000,"stock":35},
    {"nom":"lessive","prix":5000,"stock":0},
]
with open("magasin.json", "w") as f:
    json.dump(magasin, f)
print("fichier json créer !")

with open("magasin.json", "r") as f:
   data= json.load(f)
for magasine in data:
    print(magasine)
with open("magasin.json", 'r') as f:
    for magasine in data:
        if magasine['stock']>= 0:
            print(f"{magasine['nom']}")
            
big=max(magasin, key=lambda e:e['prix'])
print(f"{big['nom']}:{big['prix']}")
somme=0
moy=0
with open("magasin.json", "r") as f:
    for magasin in data:
        somme += magasine['prix']
    moy= somme / len(magasin)
    print(somme)
    print(moy)
    