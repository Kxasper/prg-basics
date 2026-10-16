#zle, przez angielski i brak wiedzy
liczba=(input("Podaj liczbę dzisiętną: "))
liczba_bin=''
for x in liczba:
    x=int(x)
    wynik1=x/2
    wynik2=wynik1**2
    x=str(x)
    liczba_bin+=x
print(liczba_bin)