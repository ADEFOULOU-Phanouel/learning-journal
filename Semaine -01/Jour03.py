 # Boucles for
for i in range(5):
    print(f"tour numéro {i}")
# Boucles for sur liste
fruits=["Pomme","Banane", "mangue"]
for fruit in fruits:
    print(f"J'aime les {fruit}s")
# Boucles while
compteur=0
while compteur<5:
    print(f"compteur:{compteur}")
    compteur = compteur+1
# Mini-défi
n=int(input("entrez un nomre: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")