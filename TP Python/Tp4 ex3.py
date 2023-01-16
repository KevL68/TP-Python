nMax = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? : "))
v1 = []
v2 = []

for i in range (0, nMax):
    v1.append(int(input("V1 : ")))

for i in range (0, nMax):
    v2.append(int(input("V2 : ")))

resultat = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print("Le produit scalaire de v1 par v2 vaut",resultat)
