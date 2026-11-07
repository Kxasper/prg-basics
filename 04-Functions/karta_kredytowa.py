def ukryj(numer):
    numer=str(numer)
    real_numer=''
    if len(numer)==16:
        real_numer+=numer[0:2]
        for x in numer[2:12]:
            x='*'
            real_numer+=x
        real_numer+=numer[12:16]
        return real_numer
    else:
        return "Zły numer karty"

if __name__=='__main__':
    print(ukryj(5290312400019022))
