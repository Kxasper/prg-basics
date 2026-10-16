#chyba git
liczba=int(input("Podaj liczbę kupiponych przedmiotów: "))
cena=int(input("Podaj cene kupionych przedmiotów: "))
laczna_cena=0

if liczba>2:
    laczna_cena=cena*2+cena*((liczba-2)*0.75)
else:
    laczna_cena=cena*liczba

print(f"Liczba kupionych produktów wynosi: {liczba}")
print(f"Cena produktu: {cena}")
print(f"Do zapłaty: {laczna_cena}")



