class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
        
class Client(Personne):
    def __init__(self, nom, age, chambre, duree_sejour):
        super().__init__(nom, age)
        self.chambre = chambre
        self.duree_sejour = duree_sejour
        
    def get_info(self):
        print(f"je m'appelle {self.nom}. J'ai {self.age} ans. j'occupe la chambre {self.chambre} pendant {self.duree_sejour}")
        
    def __str__(self):
        return(f"{self.nom}:{self.age}:{self.chambre}:{self.duree_sejour}")
    
    def est_longue_duree(self):
        if self.duree_sejour > 7:
            return True
        else:
            return False
class Employe(Personne):
    def __init__(self, nom, age, poste, salaire):
        super().__init__(nom, age)
        self.poste = poste
        self.salaire = salaire
        
    def travailler(self):
        print(f"je m'appelle {self.nom}. J'ai {self.age} ans. je suis {self.poste} et je gagne {self.salaire}")
        
    def calculer_prime(self, taux=10):
        result = (self.salaire * taux) /100
        return result
    
class Hotel:
    def __init__(self, nom):
        self.nom = nom
        self.liste_client = []
        self.employes = []
    
    def ajouter_clients(self, clients):
        self.liste_client.append(clients)
        print(f" Clients ajoutés. Client: {clients.nom}")
    
    def ajouter_employes(self, employe):
        self.employes.append(employe)
        print(f" employes ajoutés. employes: {employe.nom}")
        
    def afficher_rapport(self):
        print("---rapport clients---")
        for c in self.liste_client:
            print(f"{c.nom}:{c.chambre}:{c.age}:{c.duree_sejour}")
        print("---rapport employés---")
        for e in self.employes:
            print(f"{e.nom}:{e.poste}:{e.salaire}")
            
    def nombre_clients(self):
        return(len(self.liste_client))
        
c1 = Client("sarah",18, "A2", 9)
c2 = Client("jean",21, "G1", 3)
c3 = Client("anna",23, "O7", 12)
    
m1 = Employe("issac",30, "DRH", 2000000)
m2 = Employe("ruth",25, "DI", 4000000)
hotel = Hotel("Nom de l'hôtel")
    
c1.se_presenter()
c1.get_info()
print(c1.est_longue_duree())
    
hotel.ajouter_clients(c1)
c2.se_presenter()
c2.get_info()
print(c2.est_longue_duree())
    
hotel.ajouter_clients(c2)
c3.se_presenter()
c3.get_info()
print(c3.est_longue_duree())
    
hotel.ajouter_clients(c3)
m1.se_presenter()
m1.travailler()
print(m1.calculer_prime())
    
hotel.ajouter_employes(m1)
m2.se_presenter()
m2.travailler()
print(m2.calculer_prime())
print(hotel.nombre_clients())
    
hotel.ajouter_employes(m2)
hotel.afficher_rapport()
import json
with open("client.json","w") as f:
    json.dump([vars(p) for p in hotel.liste_client], f, ensure_ascii=False, indent=2)
    print("fichier sauvegarder !")
    
import datetime
jour = datetime.date.today()
print(f"le rapport a été généré le {jour}")
import random
numéro_réservation = random.randint(1000,9999)
print(numéro_réservation)
import os
os.makedirs("rapport_hotel/", exist_ok=True)
print("dossier créer !")



    



    
    



    
        

        
        
        
    
    
    
    



    
