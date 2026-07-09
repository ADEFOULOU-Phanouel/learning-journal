# Exo final sur semaine 1,2 et 3
def creer_employe(nom, salaire, departement="informatique"):
    return{"nom":nom,"salaire":salaire, "departement":departement}
print(creer_employe("phanouel",1000000,))

def prime(salaire):
    if salaire>=500000:
        return 500
    elif salaire>=300000:
        return 300
    else:
        return 100
print(prime(1000000))
employee=[
    creer_employe("phanouel",10000000),
    creer_employe("lisa", 10000, "juridique"),
    creer_employe("marc", 50000,"finance"),
    creer_employe("elsa",90000)
]
print(employee)
for employe in employee:
    m=prime(employe['salaire'])
    print(f"{employe['nom']} - {employe['departement']} - {m}")