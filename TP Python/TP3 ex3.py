import random

x = random.randint(0, 100)

count = 0

guess = int(input("Devinez le nombre mystère (entre 0 et 100) : "))

while guess != x:
  count += 1
  if guess > x:
    print("Le nombre mystère est plus petit")
  else:
    print("Le nombre mystère est plus grand")
  guess = int(input("Devinez à nouveau : "))

print(f"Bravo, vous avez trouvé le nombre mystère en {count} tours !")
