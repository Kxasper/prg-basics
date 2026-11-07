#dobrze, ale musiałem zobaczyc jak sie odwraca tekst
def palinidrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False

print(palinidrome("radar"))
print(palinidrome("12-11-21"))
print(palinidrome("book"))
