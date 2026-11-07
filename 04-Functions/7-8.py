#wygląda okej 
def f(amount_to_pay):
    amount_to_pay=int(amount_to_pay)
    monety=0
    while amount_to_pay>=5:
        amount_to_pay=amount_to_pay-5
        monety+=1
    while amount_to_pay>1:
        amount_to_pay=amount_to_pay-2
        monety+=1
    while amount_to_pay>0:
        amount_to_pay=amount_to_pay-1
        monety+=1
    return monety

print(f(23))
print(f(8))
print(f(2))
print(f(0))
