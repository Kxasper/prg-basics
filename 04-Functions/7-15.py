#chyba git wymyśliłem, przynajmniej wyniki się zgadzają
def f(detector):
    licznik=0
    warunek=False
    for x in detector:
        if x=="+":
            licznik+=1
            if licznik>=3:
                warunek=True
                break
        elif x=="-":
            licznik-=1
    return warunek
    
   

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
