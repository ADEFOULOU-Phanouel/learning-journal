# Tuples
point = (3, 7)
print(f"x={point[0]}, y = {point[1]}")

personne = ("Phanouel", 19, "Cotonou")
nom, age, ville = personne
print(f"{nom} a {age} ans et vit a {ville}")

# Sets
notes = {15, 12, 18, 15, 9, 12, 18}
print(f"Notes uniques : {notes}")
print(f"Nombre de notes uniques : {len(notes)}")

notes.add(20)
print(f"après ajout : {notes}")

# Opérations
matieres_s1= {"Maths", "Physique", "Info", "Anglais"}
matieres_s2= {"Info", "Anglais", "Chimie", "Sport"}

print(f"Communes: {matieres_s1 & matieres_s2}")
print(f"Toutes: {matieres_s1 | matieres_s2 }")
print(f"Seulement s1: {matieres_s1 - matieres_s2}")

# Mini-défi
notes = [9, 11, 15 , 13, 19, 9, 11, 15, 13, 19]
notes_uniques = set(notes)
print(f"notes uniques:{notes_uniques}")
etudiant = ("richard", 20, "IA")
nom, age, filiere = etudiant
print(f"{nom} a {age} ans et étudie en {filiere}")

cordonné = (1, 4)
print(f"x={cordonné[0]}, y={cordonné[1]}")
resto1= {"thé", "cafée", "degue", "apkan","igname pilé"}
resto2= {"Riz", "pates", "ragou", "soupe", "igname pilé"}
print(f"communes: {resto1 & resto2}")
print(f"toutes: {resto1 | resto2} ")
print(f"seulement resto1: {resto1 - resto2}")
print(f"seulement resto2: {resto2 - resto1}")
