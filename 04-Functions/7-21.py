#bardzo na około ale chyba działa
def f(number1,number2,number3):
    najwieksza=0
    najmniejsza=0
    suma=0
    if number1<=number2 and number1<=number3:
        najmniejsza=number1
    if number2<=number1 and number2<=number3:
        najmniejsza=number2
    if number3<=number1 and number3<=number2:
        najmniejsza=number3
    if number1>=number2 and number1>=number3:
        najwieksza=number1
    if number2>=number1 and number2>=number3:
        najwieksza=number2
    if number3>=number1 and number3>=number2:
        najwieksza=number3
    suma=najwieksza-najmniejsza
    return suma

print(f(7,4,9))
print(f(2,12,8))
