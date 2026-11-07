#nwm jak to zrobic
def f(dice):
    max_liczba=dice[0]
    max_seria=1

    aktualna_liczba=dice[0]
    aktualna_seria=1

    for i in range(1, len(dice)):
        if dice[i]==dice[i-1]:
            aktualna_seria+=1
            if aktualna_seria>max_seria:
                max_seria=aktualna_seria
                max_liczba=dice[i]
        else:
            aktualna_liczba=dice[i]
            aktualna_seria=1
    return int(max_liczba)

print(f('5233165554211'))
print(f("2133"))
