#szybciutko i łatwiutko
def f(number1, number2, operator):
    suma=0
    if operator=='+':
        suma=number1+number2
    elif operator=='-':
        suma=number1-number2
    elif operator=='*':
        suma=number1*number2
    elif operator=='**':
        suma=number1**number2
    elif operator=='%':
        suma=number1%number2
    else:
        suma=0
    return suma

print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))

