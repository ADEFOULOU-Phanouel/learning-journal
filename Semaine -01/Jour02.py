# types de variables
age= 19 # int ou entier
prenom= "Phanouel" # str ou chaine de caractère
taille= 1.82 # float ou décimal
est_majeur= True # booléen ou vrai ou faux
print(type(age))
print(type(prenom))
print(type(taille))
print(type(est_majeur))


# Les conditions
note = 14

if note >= 16:
    print("Très bien !")
elif note >= 12:
    print("Bien, continue !")
elif note >= 10:
    print("Passable")
else:
    print("Il faut travailler")

# Demander une info à l'utilisateur
prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))

if age >= 18:
    print(f"Bienvenue {prenom}, tu es majeur !")
else:
    print(f"Salut {prenom}, encore {18 - age} ans avant d'être majeur !")
    
# Mini-défi
note = int(input("Entrez votre note: "))
if note >=10:
    print("Reçu")
else:
    print("recalé")
