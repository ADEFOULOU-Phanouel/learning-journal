# Gestion des erreurs
# Eemple 1 : Erreur de conversation
try:
    nombre = int(input("Tape un nombre: "))
    print(f"Ton nombre x 2 ={nombre * 2}")
except:
    print("Erreur ! ce n'est pas un nombre !")
    
# Exemple 2: Fichier introuvable
try:
    with open("fichier_inexistant.txt","r") as f:
        contenu=f.read()
except FileNotFoundError:
    print("Erreur ! Le fichier n'existe pas")
    
# Exemple 3: Division par zéro
try:
    a= int(input("Numérateur : "))
    b= int(input("dénominateur: "))
    resultat = a / b
    print(f"réultat :{resultat}")
except ZeroDivisionError:
    print("Erreur ! Division par zero impossible !")
except ValueError:
    print("Erreur ! Tape des nombres !")
# Mini-défi
try:
    use = int(input("entrez un nombre: "))
    résultat=100/use
    print(f"résultat : {résultat}")
except ZeroDivisionError:
    print("Erreur ! Le nombre ne peut etre divisée par zéro !")
except ValueError:
    print("Erreur! entrez un nombre !")
    