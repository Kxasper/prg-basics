#nwm jak to zrobix
N = int(input("Enter N: "))
print(f"Prime numbers up to {N}:", end=" ")

for num in range(2, N + 1):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")