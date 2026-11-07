#nwm za bardzo o co tu chodzi, chyba jakaś suma liczb pierweszych ale nwm
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def f(n):
    znalezione=0
    liczba=2
    while True:
        if czy_pierwsza(liczba):
            znalezione+=1
            if znalezione==n:
                return liczba
        liczba+=1

print(f(1))
print(f(5))
