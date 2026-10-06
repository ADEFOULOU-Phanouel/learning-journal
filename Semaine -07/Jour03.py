# Jour 03: maps, filter et lambda (lambda: fonction anonyme)
# Fonction classique
def doubler(X):
    return X * 2

# Lambda équivalente
doubler = lambda X: X * 2
print(doubler(5))

# map(): transformer chaque élément 
notes = [12, 8, 15, 6, 18]
# Ajouter 2 point a chaque note
notes_bonus = list(map(lambda n: n + 2, notes))
print(notes_bonus)
notes = [12, 8, 15, 6, 18, 10, 14]
# Garder seulement les notes >= 10
admis = list(filter(lambda n : n>=10, notes))
print(admis)

# Combiner map + filter
notes = [12, 8, 15, 6, 18, 10, 14]
# D'abord filtrer les admis , ensuite ajouter un point bonus
resultat = list(map(lambda n: n+1, filter(lambda n: n >=10, notes)))
print(resultat)

# Mini-défi
employes = [
    {"nom":"Alice","Salaire":250000},
    {"nom":"Bob","Salaire":180000},
    {"nom":"Clara","Salaire":320000},
    {"nom":"David","Salaire":150000},
    {"nom":"Eva","Salaire":400000}
]

