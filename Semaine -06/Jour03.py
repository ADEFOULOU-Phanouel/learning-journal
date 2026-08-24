# Classe parent
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print(f"je suis {self.nom} et j'ai {self.age} ans")
    
    def manger(self):
        print(f"{self.nom} est en traint de manger")
        
    # classe enfant _ hérite de Animal
class Chien(Animal):
    def __init__(self,nom, age, race):
        super().__init__(nom, age) # Appelle init du parent
        self.race = race
        
    def aboyer(self):
        print(f"{self.nom} dit : wouf !")
        
    def se_presenter(self):# redéfinir la méthode du parent
        print(f"Je suis {self.nom} , un {self.race} de {self.age} ans")
        
class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur
    
    def miauler(self):
        print(f"{self.nom} dit : Miou !")
    
# créer des objets
a1 = Chien("Rex", 3, "Berger allemand")
a2 = Chat("mimi", 2, "noir")

a1.se_presenter() # méthode redéfinir
a1.manger() # méthode hérité des parents
a1.aboyer() # méthode propre au chien
a2.se_presenter() # méthode du parent
a2.manger() # méthode hérité
a2.miauler() # méthode propre au chat

# Mini-défi
class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
        
    def se_présenter(self):
        print(f"je suis {self.nom} et je gagne {self.salaire} FCFA par mois.")
        
    def calculer_prime(self, taux = 10):
        prime = (self.salaire * taux) / 100
        return (prime)
    
class Manager(Employe):
    def __init__(self, nom, salaire, equipe):
        super().__init__(nom, salaire)
        self.equipe = equipe
        
    def diriger(self):
        print(f"{self.nom} est le chef qui dirige l'équipe des {self.equipe} et il gagne {self.salaire} FCFA")

class Developpeur(Employe):
    def __init__(self, nom, salaire, langage):
        super().__init__(nom, salaire)
        self.langage = langage
        
    def coder(self):
        print(f"{self.nom} est un membre de l'équipe des dévelopeurs qui gagne {self.salaire} FCFA et qui utilise comme langage {self.langage} pour coder.")
        
e1 = Manager("éric", 1000000, "Fournisseur")
e3 =  Manager("jeanne", 800000, "Développeur")
e2 = Developpeur("mael", 500000, "python")
e4 = Developpeur("nina", 300000, "Javascript")
e1.se_présenter()
print(e1.calculer_prime(10))
e1.diriger()
e2.se_présenter()
print(e2.calculer_prime())
e2.coder()
e3.se_présenter()
print(e3.calculer_prime(10))
e3.diriger()
e4.se_présenter()
print(e4.calculer_prime())
e4.coder()
    
    
        
    
        
     