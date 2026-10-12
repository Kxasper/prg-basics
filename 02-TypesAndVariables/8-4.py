#angielski chuj wie jak to przeliczyc
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

# Przeliczamy cm na cale
total_inches = cm / 2.54

# Wyciągamy całe stopy i resztę cali
feet = int(total_inches // 12)
inches = round(total_inches % 12)

print(f"I am {cm}cm tall, i.e. {feet} feet and {inches} inches")
# Dla 170 cm wypisze: 5 feet and 7 inches