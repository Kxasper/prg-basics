#nwm dziwne to nie wiem jak to zrobic, ale blisko jestem 
def f(n):
    napis=''
    for i in range(n):
        napis+='*'
        if i<n-1:
            napis+='/'
    return napis

print(f(4))
print(f(1))