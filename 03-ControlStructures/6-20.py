#zle, przez angielski i brak wiedzy
n = int(input("Enter decimal number: "))
oryginal = n
binarny = ""

if n == 0:
      binarny = "0"

while n > 0:
      reszta = n % 2
      binarny = str(reszta) + binarny  # dopisujemy z lewej strony!
      n = n // 2

print(f"{oryginal}(10) = {binarny}(2)")