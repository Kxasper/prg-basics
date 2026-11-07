#nwm źle

wprowadzony_pin=input("Podaj pin: ")
pin='0805'
i=0

while i<3:
    wprowadzony_pin=input("Podaj pin: ")
    if wprowadzony_pin==pin:
        print("Correct pin")
        break
    else:
        print("Incorrect...")
        i+=1
        
if i==3: 
    print("Sorry, your payment card has been blocked.")