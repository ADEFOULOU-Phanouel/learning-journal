# Définir une classe
class Etudiant:
    
    def __init__(self, nom, age, note):
        self.nom = nom  # Attribut
        self.age = age # Attribut
        self.note = note # Attribut
    
    def se_présenter(self):
        print(f" Je m'appelle {self.nom} et j'ai {self.age} ans")
    
    def est_admis(self):
        if self.note>= 10:
            return True
        else:
            return False
# Créer des objets
e1 = Etudiant("Phanouel", 19, 15)
e2 = Etudiant("Phanouel", 17, 8)
e3 = Etudiant("Marc", 20, 12)
# Accéder au attribut
print(e1.nom)
print(e1.note)

# Utiliser le résultat
print(e1.est_admis()) # True
print(e2.est_admis()) # False

# boucles sur une liste d'objets
etudiant = [e1, e2, e3]
for e in etudiant:
    print(f"{e.nom} : {e.note}/20 -> admis: {e.est_admis()}")
    
# Mini-défi
class Produit:
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock
        
    def est_disponible(self): 
        if self.stock>0:
            return True
        else:
            return False
    
    def appliquer_remise(self, remise = 5):
        result = self.prix - (self.prix * remise)/100
        return(result)
 
p1 = Produit("Riz",2000, 20)
p2 = Produit("clou", 3500, 400)
p3 = Produit("pc", 80000, 70)
print(f"{p1.nom}:{p1.stock}")
print(p2.est_disponible())
print(p3.appliquer_remise(5))

produit = [p1,p2,p3]
for e in produit:
    print(f"{e.nom} : {e.stock} --> est disponible:{e.est_disponible()} --> appliquer remise: {e.appliquer_remise(5)}")



    
    