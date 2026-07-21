# créer un dictionnaire
personne={
    "prenom":"Phanouel",
    "age":19,
    "ville":"cotonou"
    }
# Accéder a une valeur
print(personne["prenom"])
print(personne["age"])
# Modifier une valeur
personne["age"]=20
print(personne["age"])
# Ajouter une nouvelle clée
personne["email"]="phanouel@gmail.com"
print(personne)
# Parcourir un dictionnaire
for cle,valeur in personne.items():
    print(f"{cle} : {valeur}")
# Mini-défi
etudiant={"nom":"Phanouel",
          "age":20,
          "filiere":"informatique",
          "moyenne":14}
print(f"{etudiant["nom"]} a une moyenne de {etudiant["moyenne"]}/20 en {etudiant["filiere"]}")
