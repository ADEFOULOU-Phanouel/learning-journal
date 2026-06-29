# fonction qui retourne un résultat
def saluer(prenom):
    print(f"Bonjour, {prenom} !")
saluer("Phanouel")
saluer("Alice")
# fonction qui retourne un résultat
def addition(a,b):
    return a+b
resultat = addition(5, 3)
print(f"Le résultat de l'addition est: {resultat}")
# Mini-défi
def est_pair(nombre):
    if nombre% 2==0:
        print("pair")
    else:
        print("impair")
est_pair(3)
est_pair(4)