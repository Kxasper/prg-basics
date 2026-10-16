#git
czas=int(input("Podaj liczbę godzin spędzonych na parkingu: "))
cena=0

if 1<=czas<=2:
    cena=5
elif 3<=czas<=6:
    cena=15
elif czas>6:
    cena=20

print(f"Liczba godzin spędzonych na parkingu to {czas}, co kosztuje {cena}PLN")