# partie 1 _ class parent
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        print(f"je m'appelle {self.nom} et j'ai {self.age} ans.")
        
# Partie 2 _ class enfant
class Patient(Personne):
    def __init__(self, nom, age, maladie, chambre):
        super().__init__(nom, age)
        self.maladie = maladie
        self.chambre = chambre
    def get_chambre(self):
        print(f"le patient inscrit au nom de {self.nom} et agée de {self.age} ans est atteit de {self.maladie} et occupe la chambre {self.chambre}")
        
    def est_grave(self):
        if self.maladie == 'grave':
            return True
        else:
            return False 
    def __str__(self):                          
        return f"{self.nom} (chambre {self.chambre})"
class Medecin(Personne):
    def __init__(self, nom, age,specialiste, salaire):
        super().__init__(nom, age)
        self.specialiste = specialiste
        self.salaire = salaire
        
    def consulter(self):
        print(f"le médécin {self. nom} agée de {self.age} ans est reconnue comme {self. specialiste} et gagne {self.salaire} FCFA")
        
    def calculer_prime(self, taux=10):
        result = (self.salaire * taux) /100
        return result
    def __str__(self):                          
        return f"{self.nom} (chambre {self.specialiste})"
    
# Partie 3 _ Classe principale
class Clinique:
    def __init__(self, nom):
        self.nom = nom
        self.patients = []
        self.medecins = []
        
    def ajouter_patient(self, patient):
        self.patients.append(patient)
        print(f"patient ajouter. patient: {patient.nom}")
    
    def __str__(self):
        return f"Clinique {self.nom} — {len(self.patients)} patients, {len(self.medecins)} médecins"
    
    def ajouter_medecin(self, medecin):
            self.medecins.append(medecin)
            print(f"medecin ajouter. Medecin: {medecin.nom}")
            
    def afficher_rapport(self):
        print("--- Patients ---")
        for p in self.patients:
            print(f"{p.nom} : {p.chambre}")
        print("--- medecins ---")
        for m in self.medecins:
            print(f"{m.nom} : {m.specialiste}-prime :{m.calculer_prime()}")

        
    def nombre_patients(self):
        return (f"{len(self.patients)}")
    
p1 = Patient("awa",20, "cancer","A2")
p2 = Patient("marc", 23, "Grippe", "G5")
p3 = Patient("anna",18, "Paludisme", "I4") 

m1 = Medecin("Luc",22, "cardiologue", 50000000)
m2 = Medecin("sarah", 23, "Médécin généraliste", 1000000)
clinique = Clinique("Clinique du Port") 

clinique.ajouter_patient(p1)
clinique.ajouter_patient(p2)
clinique.ajouter_patient(p3)
clinique.ajouter_medecin(m1)
clinique.ajouter_medecin(m2)
clinique.afficher_rapport()
print(clinique.nombre_patients())   
print(m1.calculer_prime())
print(m2.calculer_prime())




import json
with open("patients.json", "w") as f:
    json.dump([vars(p) for p in clinique.patients], f, ensure_ascii=False, indent=2)
print("fichier sauvegarder !")
import datetime
jour = datetime.date.today()
print(f"ce rapport a été généré le {jour}")
import random
numéro_dossier = random.randint(1000,9999)
print(f"numéro de dossier : {numéro_dossier}")
import os
os.makedirs("rapport_clinique/", exist_ok=True)
print("Dossier créer !")   


     