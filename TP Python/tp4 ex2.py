nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range (0, nombreEtudiants):
    note = float(input(f"Note étudient {i} : "))
    notes.append(note)

moyenne_classe =  note / nombreEtudiants

print("Moyenne de classe :", moyenne_classe)

print("Numéro de l'étudiant | note | ecart à la moyenne")
for i, grade in enumerate(notes):
    deviation = note - moyenne_classe
    print(f"{i} | {note:.1f} | {deviation:.2f}")