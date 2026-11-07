#set sprawdzone w necie bo nie wiedziałem tego
def f(password):
    password=str(password)
    if len(password)>=6 and len(password)==len(set(password)):
        return True
    else:
        return False

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))



