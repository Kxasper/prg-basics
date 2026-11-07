#git
wiek=int(input("Podaj swój wiek: "))
status=''
if wiek<13:
    status='Dziecko'
elif 13<=wiek<=19:
    status='Nastolatek'
elif 20<=wiek<=64:
    status='Dorosły'
elif wiek>=65:
    status='Senior'
print(f"Należysz do grupy {status}, ponieważ masz {wiek} lat.")