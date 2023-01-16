somme = int(input("Entrez la somme d'argent à décomposer : "))
nb_100 = somme // 100
somme = somme % 100
nb_50 = somme // 50
somme = somme % 50
nb_10 = somme // 10
somme = somme % 10
nb_2 = somme // 2
somme = somme % 2
nb_1 = somme
print("Décomposition de la somme :")
print(f"{nb_100} billets de 100")
print(f"{nb_50} billets de 50")
print(f"{nb_10} billets de 10")
print(f"{nb_2} pièces de 2")
print(f"{nb_1} pièces de 1")
