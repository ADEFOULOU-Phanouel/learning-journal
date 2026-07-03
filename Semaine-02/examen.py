# Sujet: Gestion d'une école
# Partie 1: Variables et condition
nom_ecole= "emeraude"
année_en_cour=2026
nombres_eleves=400
print(f"l'école {nom_ecole} à {nombres_eleves} élèves en {année_en_cour}")
if nombres_eleves>100:
    print(f"grande école:",nom_ecole)
else:
    print(f"petite école :", nom_ecole)
    
# partie 2: Boucles
matieres=["mathématiques","svt","pct","francais","anglais"]
i=0
for matiere in matieres:
    i+=1
    print(f"matiere {i+0}: {matiere}")
print(f"nombres de matiere:{len(matieres)}")
# partie 3: Fonctions
def mention(note):
    if note>=16:
        print("excellent")
    elif note>=14:
        print("bien")
    elif note>=12:
        print("Assez-bien")
    elif note>=10:
        print("Passable")
    else:
        print("insuffisant")
mention(15)
mention(5)
mention(19)
# partie 4: Listes des dictionnaires
eleves=[
    {"nom":"max","age":15,"note":13},
    {"nom":"elene","age":16,"note":7},
    {"nom":"david","age":14,"note":18},
    {"nom":"rahab","age":14,"note":8},
    {"nom":"anabelle","age":15,"note":15}
]
for eleve in eleves:
    print(f"{eleve['nom']}")
print("admis")
for eleve in eleves:
    if eleve['note']>=10:
        print(f"{eleve["nom"]}:{eleve["note"]}")
print("meilleur élève")
meilleur=  max(eleves,key=lambda e:e["note"])
print(f"{meilleur['nom']}: {meilleur['note']}")

somme=0
for eleve in eleves:
    somme+=eleve['note']
    moy=somme/ len(eleves)
print(somme)
print(moy)

    

    