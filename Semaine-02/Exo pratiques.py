"""
# Exo dictionnaire
amis=['Piérick','Mickael','Osée', 'Anselme']
# Dictionnaire
meilleure_amie = {
    "nom":"Anselme",
    "Age":20,
    "Ville":"Calavi"
}
for i in amis:
    print(i)
for clee,valeur in meilleure_amie.items():
    print(f"{clee}:{valeur}")
    
# Exo 2
somme=0
moy=0
nombres = [0,1,2,3,4]
for i in nombres:
    somme+=i
print(f"somme:", somme)
moy= int(somme/len(nombres))
print(f"moy:",moy)
print(f"max:",max(nombres))
"""
def mention(note):
    if note>=16:
        print("excellent")
    elif note>=14:
        print("bien")
    elif note>=12:
        print("Assez bien")
    elif note>=10:
        print("passable")
    else:
        print("Insuffissant")
mention(15)
