#moim sposobem ale raczej działa
def f(n1,n2,n3):
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    warunek=True
    if n1>=0 and n2>=0 and n3>=0:
        warunek=False
    else:
        warunek=True
    return warunek

print(f(11,6,-4))
print(f(5,4,14))
