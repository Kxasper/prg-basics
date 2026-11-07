import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
cale = converters.cm_to_ih(100)
print(f"100 cm to {cale:.2f} cali")
wzrost_cm = converters.feet_and_in_to_cm(5, 11)
print(f"5 stóp i 11 cali to {wzrost_cm:.2f} cm")
