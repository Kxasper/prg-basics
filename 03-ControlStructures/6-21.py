#zle, ale kurde blisko jestem
cena=int(input("Enter the amount in PLN: "))
liczba_5=0
liczba_2=0
liczba_1=0
while cena-5>0:
    cena-=5
    liczba_5+=1
while cena-2>0:
    cena-=2
    liczba_2+=1
while cena-1>0:
        cena-=1
        liczba_1+=1
print(f"5 PLN coins: {liczba_5}")
print(f"2 PLN coins: {liczba_2}")
print(f"1 PLN coins: {liczba_1}")


