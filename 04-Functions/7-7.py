#nwm w sumie, ale długo nad tym siedziałem i chyba działa
def czy_binarna(liczba):
    liczba=str(liczba)
    warunek=False
    for x in liczba:
        if x=='0' or x=='1':
            warunek=True
        else:
            warunek=False
            break
    return warunek

print(czy_binarna('101101'))
print(czy_binarna('1311a10100'))

