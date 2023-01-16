string = input("Entrez un mot ou une phrase : ")

string = ''.join([c for c in string.lower() if c.isalpha()])

if string == string[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
