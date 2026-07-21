# Module intégrés
# module math
import math

print(math.sqrt(25))  # racine carrée -> 5.0
print(math.pi)  # valeur de pi -> 3.14159...
print(math.ceil(4.3)) # arrondi supérieure -> 5
print(math.floor(4.9)) # Arrondi inférieur -> 4

# Module random
import random
print(random.randint(1,10)) # Nombre aléatoire entre 1 et 10
print(random.choice(["rouge", "bleu", "vert"])) # choix aléatoire

# Module datetime
import datetime
aujourd_hui = datetime.date.today()
print(f"aujoud'hui : {aujourd_hui}")

maintenant = datetime.datetime. now()
print(f"il est : {maintenant.hour}h{maintenant.minute}")

# Mini-défi
import random
nombres = [] 
somme = 0
for i in range (5):
   m = int(random.randint(1,100))
   nombres.append(m)
   somme+=m
   print(m)
moy= somme / len(nombres)
   
print(nombres)
print(f"Le plus grand:{max(nombres)}")
print(f"le plus petit:{min(nombres)}")
print(somme)
print(moy)
print(f"moyenne:{sum(nombres)/len(nombres)}")  

# défi
# Patie 1: Module math
import math
m = float(input("entrez un nombre décimale: "))
print(f"racine carrée de m:{math.sqrt(m)}")
print(f"nombre arrondi supérieur de m:{math.ceil(m)}")
print(f"nombre arrondi inférieur de m:{math.floor(m)}")
print(f"multiplication de m par pie:{math.pi * m}")

# Partie 2: Module random
import random
notes=[]
for i in range(8):
   n = random.randint(0, 20)
   notes.append(n)
print(notes)
print(f"le maximum de n:{max(notes)}")
print(f"le minimum de n : {min(notes)}")
print(f"la moyenne de la classe est: {sum(notes)/len(notes)}")
   
nom = ["Luc", "marc", "jean", "loan", "pierre"]
print(f"l'élève de la semaine est: {random.choice(nom)}")

# Partie 3: module datetime
import datetime
jour = datetime.date.today()
print(f"la date d'aujourd'hui est : {jour}")
h = (datetime.datetime.now())
print(f"l'heure actuelle est: {h.hour}:{h.minute}")
noel = datetime.date(jour.year, 12 ,25)
jour_restant = (noel - jour).days
print(f"le nombre de jour restant avant noel est:{jour_restant} jour")

# partie 4: conbinaison
import math
import random
import datetime
def mention(note):
   if note>=18:
      return("mention excellente")
   elif note>=16:
      return("mention très bien")
   elif note>=14:
      return("mention bien")
   elif note>=12:
      return("mention assez bien")
   elif note>=10:
      return("mention passable")
   else:
      return("mention insuffisante")
for note in  notes :
   print(f"note: {note}->{mention(note)}")

with open("note_semaine5.txt", "w") as f:
   for note in notes:
      f.write(f"{notes}/n")
   print("fichier sauvegarder !")























