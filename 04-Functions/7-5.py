#wygląda też dobrze
import czy_jest_z_zakresu

liczba=int(input("Wybierz liczbę: "))
zakres=' '
if czy_jest_z_zakresu.zakres(liczba):
    zakres='tak'
else:
    zakres='nie'
    

print(f'Liczba {liczba} jest w zakresie <2,15>: {zakres}')