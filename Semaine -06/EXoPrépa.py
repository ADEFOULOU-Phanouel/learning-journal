# Partie 1 _ Classes et objets
class Voiture:
    def __init__(self, marque, modele, vitesse_max, kilometrage = 0):
        self.marque = marque
        self.modele = modele
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage
    
    def se_presenter(self):
        print(f"cette voiture est une marque {self.marque} dont le modèle est {self.modele} avec une vitesse maximal de {self.vitesse_max}.")
    
    def est_rapide(self):
        if self.vitesse_max >150:
            return True
        else:
            return False
    def rouler(self, Km):
        self.kilometrage += Km
        print(f"kilometrage {Km} ajouté. kilomètre parcourue: {self.kilometrage}")
    def afficher_kilometrage(self):
        print(f"le kilometrage total de la voiture de marque {self.marque}, de modèle {self.modele} et d'une vitesse maximale de {self.vitesse_max} est de {self.kilometrage} ")
            

    
v1 =Voiture("Toyota","Corolla", 180)
v2 = Voiture("Renault", "Zoe", 140)
v3 = Voiture("Ferrari", "F40", 324)
print(f"{v1.marque} : {v1.modele} : {v1.vitesse_max}")
print(f"{v2.marque }: {v2.modele} : {v2.vitesse_max}")
print(f"{v3.marque }: {v3.modele} : {v3.vitesse_max}") 
v1.se_presenter()
print(v1.est_rapide())   
v2.se_presenter()
print(v2.est_rapide()) 
v3.se_presenter()
print(v3.est_rapide()) 
v1.rouler(700)
v2.rouler(200)
v3.rouler(500)
v1.afficher_kilometrage()
v2.afficher_kilometrage()
v3.afficher_kilometrage()

class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, vitesse_max, baterrie, kilometrage = 0):
        super().__init__( marque, modele, vitesse_max, kilometrage = 0)
        self.baterrie = baterrie
        
    def recharger(self):
        print(f"{self.marque} {self.modele} est en cour de recharge... baterrie : {self.baterrie}%")
    
class VoitureSport(Voiture):
    def __init__(self, marque, modele, vitesse_max, turbo=True, kilometrage = 0):
        super().__init__( marque, modele, vitesse_max, kilometrage = 0)
        self.turbo = turbo
        
    def accelerer(self):
        print(f"{self.marque} {self.modele} accélère avec le turbo... turbo : {self.turbo}")
        
e1 = VoitureElectrique("Porsche",911,324,25,500)
e2 = VoitureElectrique("tesla","modèle 3",225,75,900)
s1 = VoitureSport("peugeot", 308, 175,125, 800 )
s2 = VoitureSport("tesla","modèle 3",225,75, )
e1.se_presenter()
e1.est_rapide()
e1.rouler(800)
e1.afficher_kilometrage()
e1.recharger()
e2.se_presenter()
e2.est_rapide()
e2.rouler(200)
e2.afficher_kilometrage()
e2.recharger()
s1.se_presenter()
s1.est_rapide()
s1.rouler(400)
s1.afficher_kilometrage()
s1.accelerer()
s2.se_presenter()
s2.est_rapide()
s2.rouler(600)
s2.afficher_kilometrage()
s2.accelerer()




            
    
 


    