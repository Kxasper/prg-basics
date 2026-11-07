#idealnie
def f(name):
    tekst=''
    for x in name.split():
        tekst+=x[0]
    return tekst

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))
