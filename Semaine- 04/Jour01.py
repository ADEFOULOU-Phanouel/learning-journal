# Ecrire dans un fichier
# "W" = write("ecrire") ___ créer le fichier s'il n'existe pas
with open("notes.txt", "w") as f:
    f.write("Phanouel : 15\n") # \n = retour a la ligne
    f.write("alice : 12\n")
    f.write("marc : 18\n")
print("Fichier créé !")

# Lire tout les fichier d'un coup
# "r" = read(lire)
with open("notes.txt", "r") as f:
    contenu=f.read() # lit tout le contenu
print(contenu)

# Lire ligne par ligne
with open("notes.txt", "r") as f:
    for ligne in f:
        print(ligne.strip()) # enlève les espaces et \n en trop

# Ajouter sans effacer
# "a" = append(ajouter)
with open("notes.txt", "a") as f:
    f.write("sarah : 16\n")
print("Sarah ajoutée !")
# Mini-défi
with open("eleves.txt", "w") as f:
    f.write("luc: 3\n"),
    f.write("marc : 8\n"),    
    f.write("eric: 11\n"),
    f.write("nick: 14\n"),
    f.write("tom: 18\n")
print("fichier créer !")
with open("eleves.txt", "r") as f:
    contenu=f.read()
    print(contenu)
with open("eleves.txt", 'r') as f:
    for ligne in f:
        print(ligne.strip())
        
# Partie 2
with open("villes.txt", "w") as f:
    f.write("Abomey Calavi : 15000 \n"),
    f.write("cotonou : 20000 \n"),
    f.write("porto-novo: 10000 \n"),
    f.write("Parakou: 7000 \n")
print("fichier créer")

with open("villes.txt", "r") as f:
    contenu=f.read()
    print(contenu)
with open("villes.txt","r") as f:
    for ligne in f:
        print(ligne.strip())
with open("villes.txt", "a") as f:
    f.write("Ouidah : 3000\n")
    print("Ouidah ajouter")
with open("villes.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())

    

        