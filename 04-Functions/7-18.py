#łatwo i szybko
def f(sentence):
    zdanie=''
    for x in sentence:
        if x!=" ":
            zdanie+=x
    return zdanie

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))