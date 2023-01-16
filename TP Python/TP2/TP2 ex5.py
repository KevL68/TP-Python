x = int(input("Entrez un nombre entier : "))

if x % 2 == 0 and x < 0:
    print("Le nombre est pair et négatif")
elif x % 2 == 0 and x > 0:
    print("Le nombre est pair et positif")
elif x % 1 == 0 and x < 0:
    print("Le nombre est impair et négatif")
elif x % 1 == 0 and x > 0:
    print("Le nombre est impair et positif")
elif x == 0:
    print("Le nombre est zéro (et il est pair)")


