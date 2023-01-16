BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

nouvelleQuantite1 = fromage * nbConvives / BASE
nouvelleQuantite2 = eau * nbConvives / BASE
nouvelleQuantite3 = ail * nbConvives / BASE
nouvelleQuantite4 = pain * nbConvives / BASE

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut : ")
print(nouvelleQuantite1,"gr de fromage")
print(nouvelleQuantite2,"dl d'eau'")
print(nouvelleQuantite3,"gousse(s) d'ail")
print(nouvelleQuantite4,"gr de pain")

