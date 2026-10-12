#średnio (wszystko dziwne)
import math
Obwod=float(input(("Podaj obwód w cm: ")))
Srednica = Obwod/math.pi
if Srednica >= 50:
    print("Można ściąć")
else:
    print("Nie można ściąć")