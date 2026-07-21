# Créer une liste
fruits=["pomme","banane","mangue","orange"]
# Accéder a un éléments( A partir de 0)
print(fruits[0])
print(fruits[1])
print(fruits[-1])
# Taille de la liste
print(len(fruits))
# Ajout d'un élément
fruits.append("fraise")
print(fruits)
# Supprimer un élément
fruits.remove("banane")
print(fruits)
# Parcourir une liste
for fruit in fruits:
    print(f"j'aime {fruit}")
# Mini-défi
matiere = ["mathématique", "biologie", "francais", "anglais", "pct"]
print(matiere[0])
print(matiere[-1])
matiere.append("philosophie")
print(matiere)
print(len(matiere))
