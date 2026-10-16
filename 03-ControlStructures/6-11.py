#git
obecna_cena=float(input("Podaj obecną cenę produktu: "))
poprzednia_cena=float(input("Podaj poprzednią cenę produktu: "))
obnizka=(1-(obecna_cena/poprzednia_cena))*100
obnizka=round(obnizka,2)
if obnizka>=10:
    print(f"Obecna cena produktu: {obecna_cena}")
    print(f"Poprzednia cena produktu: {poprzednia_cena}")
    print(f"Kup ten produkt!!")
    print(f"Cena produktu obniżona o {obnizka}%")
else:
    print(f"Obecna cena produktu: {obecna_cena}")
    print(f"Poprzednia cena produktu: {poprzednia_cena}")
    print(f"Nie kupuj tego produktu!!")
    print(f"Cena produktu obniżona o {obnizka}%")


