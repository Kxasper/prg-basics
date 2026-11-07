#źle (nie angielski)
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')

diff=abs(ord(last)-ord(first))
number_of_letters = max(0, diff - 1)
print(f'Between {first} and {last} is {number_of_letters} letters')