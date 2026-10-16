#chyba git
car_speed=int(input("Podaj prędkość samochodu: "))
speed_limit_min=40
speed_limit_max=140

if speed_limit_min<=car_speed<=speed_limit_max:
    print("Correct speed")
elif speed_limit_max<car_speed or speed_limit_min>car_speed:
    print("Invalid car speed!!")