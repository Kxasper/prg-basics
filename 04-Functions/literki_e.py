def literki(tekst):
    liczba_e=0
    for x in tekst:
        if x=='e':
            liczba_e+=1
    return liczba_e
