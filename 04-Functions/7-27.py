#chyba git, angielski nie miałem pojęcia o co tam chodzi
def f(product_code):
    product_code=str(product_code)
    jeden=int(product_code[0])
    dwa=int(product_code[1])
    trzy=int(product_code[2])
    reszta=(jeden+dwa+trzy)%7
    if int(product_code[3])==reszta:
        return True
    return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))

