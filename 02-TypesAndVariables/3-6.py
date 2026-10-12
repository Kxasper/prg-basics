#srednio (angielski)
import math
h=int(input("Podaj wysokość: "))
d1=3.57*math.sqrt(h)
d2=3.57*math.sqrt(h+20)

print(f"Dystans z plaży: {round(d1,2)}")
print(f"Dystans z wysokości 20 metrów: {round(d2,2)}")