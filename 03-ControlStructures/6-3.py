#nie rozumiem po angielsku
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 1
if light_switch1 and light_switch2:
    bulbs_on=3
print(f"There are {bulbs_on} bulbs on, because light switch 1 is {light_switch1} and light switch 2 is {light_switch2}")