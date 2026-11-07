#szybko zrobione wygląda dobrze
def f(x,y):
    suma=0
    for i in range(x,y+1):
        if i%2==0 and i<0:
            suma+=1
    return suma





print(f(-7,8))
print(f(-1,11))