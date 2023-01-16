personnes = []

for i in range(2):
    prenom = input("Entrez le prénom de la personne {}: ".format(i + 1)).capitalize()
    nom = input("Entrez le nom de la personne {}: ".format(i + 1)).upper()
    personnes.append((nom, prenom))

personnes.sort()

for nom, prenom in personnes:
    print("{} {}".format(prenom, nom))