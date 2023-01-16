from time import sleep

n = int(input("Entre un nombre entier : "))

while(n+1):
    sleep(0.2)
    print(n)
    n=n-1