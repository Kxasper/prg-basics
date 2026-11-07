#angielski, nwm co to repeated digits - powtarzające się cyfry
#ale chyba mega proste tbh
def f(number):
    suma=0
    number=str(number)
    for x in number:
        if number.count(x)>1:
            x=int(x)
            suma+=x
    return suma

print(f(1027))
print(f(230335))
print(f(513553007))