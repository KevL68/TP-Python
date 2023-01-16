# Demande les heures de début et de fin de location à l'utilisateur
debut = int(input("Heure de début de location : "))
fin = int(input("Heure de fin de location : "))

# Vérifie que les heures entrées par l'utilisateur sont comprises entre 0 et 24
if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")

# Vérifie que l'heure de fin de location est différente de l'heure de début
elif debut == fin:
    print("Attention ! l'heure de fin est identique à l'heure de début.")

# Vérifie que l'heure de début de location est inférieure à l'heure de fin
elif debut > fin:
    print("Attention ! le début de la location est après la fin de la location.")

# Si aucune erreur n'a été détectée, calcule le coût de la location et l'affiche
else:
    # Calcul du nombre d'heures de location
    duree = fin - debut

    # Calcul du tarif de la location en fonction de l'heure de début
    if debut >= 0 and debut < 7 or debut >= 17 and debut < 24:
        tarif = duree * 1
    else:
        tarif = duree * 2

    # Affichage du coût de la location
    print("Coût de la location :", tarif, "euros")

