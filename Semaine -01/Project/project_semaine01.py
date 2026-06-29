#Calculatrice python
nombre1=int(input("entrez un premier nombre: "))
nombre2= int(input("entrez un second nombre: "))
opération=input("quel opération souhaitez vous éffectuer?: ")
if opération=='+':
    print(f"{nombre1}+{nombre2}:{nombre1+nombre2}")
elif opération=='-':
        print(f"{nombre1}-{nombre2}:{nombre1-nombre2}")
elif opération=='*':
        print(f"{nombre1}*{nombre2}:{nombre1*nombre2}")
elif opération=='/':
        print(f"{nombre1}/{nombre2}:{nombre1/nombre2}")
else:
    raise SyntaxError("fin du programme")
reponse= input("souhaiter vous recommencer(oui/non): ")
if reponse=="oui":
    print("super on reprend")
else:
    print("Ok a très bientot")

    
