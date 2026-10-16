#chyba git, przynajmniej wynik wychodzi 
wiek_psa=int(input("Podaj wiek psa: "))
normalne_lata=0
if 1<=wiek_psa<=2:
    normalne_lata=wiek_psa*10.5
elif wiek_psa>2:
    normalne_lata=wiek_psa*4-8+21
print(f"Pies ma {wiek_psa} lat, co przekłada się na {normalne_lata} lat człowieka.")