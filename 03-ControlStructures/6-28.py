a = 0
b = 1

for x in range(20):
    print(a, end=" ")
    # Obliczamy kolejny wyraz (b staje się nowym a, a suma a+b nowym b)
    a, b = b, a + b