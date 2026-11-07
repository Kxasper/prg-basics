#wygląda dobrze
def f(numer, even):
    numer=str(numer)
    suma=0
    for x in numer:
        x=int(x)
        if even==True:
            if x%2==0:
                suma+=x
        elif even==False:
            if x%2!=0:
                suma+=x
    return suma

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))
