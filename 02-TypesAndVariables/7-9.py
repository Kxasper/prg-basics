#angielski ale chyba git i fukcja random problematyczna
import random
liczba_wylosowana=random.randint(1,6)
if liczba_wylosowana==1 or liczba_wylosowana==6:
    liczba=True
else:
    liczba= False
print(f"liczba to: {liczba_wylosowana}, czy jest to 1 lub 6: {liczba}")