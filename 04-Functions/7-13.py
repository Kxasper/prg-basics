#wygląda dobrze
def f(n):
    liczba=''
    for x in range(1,n+1):
        x=str(x)
        liczba+=x
    return liczba

print(f(11))
print(f(4))