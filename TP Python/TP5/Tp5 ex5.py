heures_travaillees = int(input("Combien d'heure travaillez-vous ? : "))
salaire_horaire = int(input("Quel est votre salaire horraire ? : "))
salaire = 0
if heures_travaillees <= 160:
    salaire = heures_travaillees * salaire_horaire
elif heures_travaillees <= 200:
    salaire = (160 * salaire_horaire) + ((heures_travaillees - 160) * (salaire_horaire * 1.25))
else:
    salaire = (160 * salaire_horaire) + (40 * (salaire_horaire * 1.25)) + (
                (heures_travaillees - 200) * (salaire_horaire * 1.5))
print("Votre salaire est de :",salaire, "€")
