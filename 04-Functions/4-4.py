#srednio
def suma_cyfr(a):
    a=abs(a)
    a=str(a)
    suma=0
    for x in a:
        x=ord(x)
        suma+=x
    return suma

a=int(input("Wpisz liczbę całkowitą: "))
print(f'The sum of the digits in the number {a} is {suma_cyfr(a)}')