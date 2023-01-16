n = int(input("Entrez un nombre ! : "))
fact=1
p = 1

a = "for"
b = "while"

c = input("Quelle boucle choisisez-vous ? (for ou while) : ")

if c == a:
    for i in range(1, n+1):
        print(fact)
        fact = fact * i
    print(n, "! = ", fact)
elif c == b:
    while not (p>n):
        print(fact)
        fact *= p
        p+=1
    print(n, "! = ", fact)

