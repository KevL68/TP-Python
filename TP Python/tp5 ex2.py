notes = []

for i in range(5):
    note_coefficient = input("Veuillez entrer la note et le coefficient pour le module {} (séparez-les par un espace) : ".format(i + 1))
    note, coefficient = note_coefficient.split()
    note = float(note)
    coefficient = int(coefficient)
    notes.append((note, coefficient))

somme_notes = 0
somme_coefficients = 0

# Calcule la moyenne pondérée
for note, coefficient in notes:
    somme_notes += note * coefficient
    somme_coefficients += coefficient

moyenne_ponderee = somme_notes / somme_coefficients

# Vérifie si aucune note n'est inférieure à 8
note_inferieure_8 = False
for note, coefficient in notes:
    if note < 8:
        note_inferieure_8 = True

if moyenne_ponderee >= 10 and not note_inferieure_8:
    print("L'étudiant est admis avec une moyenne de {:.2f}".format(moyenne_ponderee))
else:
    print("L'étudiant n'est pas admis avec une moyenne de {:.2f}".format(moyenne_ponderee))
