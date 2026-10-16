#chyba git/ sprawdzilem jak sie nazywaja te boki w osiach w internecie
x=int(input("Wprowadź x: "))
y=int(input("Wprowadź y: "))

if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the secound quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x==0:
    print(f"Point P({x},{y}) is in the x-axis of the coordinate system")
elif y==0:
    print(f"Point P({x},{y}) is in the y-axis of the coordinate system")
elif x==0 and y==0:
    print(f"Point P({x},{y}) is in the middle of the coordinate system")
