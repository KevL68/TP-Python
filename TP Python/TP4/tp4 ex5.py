def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        return True
    return False

def verification_date(date_saisie):
    jour = int(date_saisie[:2])
    mois = int(date_saisie[2:4])
    annee = int(date_saisie[4:])

    if len(date_saisie) != 8:
        print("La date saisie n'est pas au bon format (jjmmaaaa)")
        return

    if mois < 1 or mois > 12:
        print("Le mois saisi n'est pas valide")
    elif jour < 1 or jour > 31:
        print("Le jour saisi n'est pas valide")
    elif (mois == 2 and (jour > 29 or (jour > 28 and not est_bissextile(annee)))):
        print("La date saisie n'est pas valide")
    elif (mois in [4, 6, 9, 11] and jour > 30):
        print("La date saisie n'est pas valide")
    else:
        print("La date saisie est valide")

date_saisie = input("Entrez une date (jjmmaaaa) : ")
verification_date(date_saisie)
