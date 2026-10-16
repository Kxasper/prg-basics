#chyba git
numer=input("Enter EAN-13 article number: ")

if len(numer)==13 and numer.isdigit():
    print("Article number is correct")
    if numer[0:2]=='590':
        print("Article manufactured in Poland")
    else:
        print("Article manufactured in other country than Poland")
else:
    print("Enter correct EAN-13 article number")