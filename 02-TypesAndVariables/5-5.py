#chujowo (nie angielski, po próbach zrobiłem)
Cena = float(input("Podaj cene:"))
Znizka_w_procentach = int(input("Podaj znizke:"))
Znizka=Cena*Znizka_w_procentach/100
Cena_ze_znizka=Cena-Znizka

print(f"Cena wejściowa: {round(Cena,2)}")
print(f"Promocja w %: {Znizka_w_procentach}%")
print(f"Cena ze zniżką: {round(Cena_ze_znizka,2)}")
print(f"Zniżka: {round(Znizka,2)}")


