class  CompteBancaire:
    
    def __init__(self, propriétaire, solde = 0):
        self.propriétaire = propriétaire
        self.solde = solde
        self.historique = [] # Ensemble vide au départ
        
    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"dépot: +{montant}")
        print(f"Dépot de {montant} éffectué. Solde : {self.solde}")
            
    def retirer(self, montant):
        if montant > self.solde:
            print("solde insuffisant")
        else:
            self.solde -= montant
            self.historique.append(f"retrait : -{montant}")
            print(f"retrait de {montant} éffectué. solde : {self.solde}")
                
    def afficher_solde(self):
        print(f"solde de {self.propriétaire} : {self.solde} FCFA")
            
    def afficher_historique(self):
        print(f"_ _ _ Historique de {self.propriétaire} _ _ _")
        for operation in self.historique:
            print(operation)
        
# créer des comptes
c1 = CompteBancaire("Phanouel", 50000)
c2 = CompteBancaire("Alice")

# Utiliser les méthodes
c1.deposer(20000)
c1.retirer(10000)
c1.retirer(100000) # solde insuffisant
c1.afficher_solde()
c1.afficher_historique()

c2.deposer(5000)
c2.afficher_solde

# Mini-défi
class Etudiant:
    
    def __init__(self, nom):
        self.nom = nom
        self.note = []
        
    def ajouter_note(self, note):
        self.note.append(note)
        print(f"note {note} ajouté. Note : {self.note}")
        
    def moyenne(self):
        self.moy = sum(self.note) / len(self.note)
        return(f"la moyenne est {self.moy:.2f}")
    
    def mention(self):
        if self.moy >16:
            return(f"{self.moy:.2f} --> mention très bien")
        elif self.moy > 14:
            return(f"{self.moy:.2f} --> mention Bien")
        elif self.moy > 12:
            return(f"{self.moy:.2f} --> mention assez-bien")
        elif self.moy > 10:
            return (f"{self.moy:.2f} --> mention passable")
        else :
            return (f"{self.moy:.2f} --> mention insuffissant")
e1 = Etudiant("eric")
e2 = Etudiant("Jeanne")
e1.ajouter_note(12)
e1.ajouter_note(15)
e1.ajouter_note(17)
e2.ajouter_note(8)
e2.ajouter_note(19)
e2.ajouter_note(13) 
print(e1.moyenne())
print(e1.mention())
print(e2.moyenne())
print(e2.mention())


        
    

         