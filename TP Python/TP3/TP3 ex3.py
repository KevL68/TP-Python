import random

n = random.randint(0,100)
x = 0
r=0
while x!=n:
        r=r+1
        x = int(input("Quel est la valeur ? "))
        if x == n:
            print("Vous avez trouver, le nombre était ", n)
        elif x > n:
                print("Le nombre est plus petit !")
        elif x<n:
            print("Le nombre est plus grand !")

print("Vous avez fait", r, "tentatives !")