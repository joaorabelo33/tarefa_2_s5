def vogais(c):
    c=c.lower()
    vogais=['a','e','i','o','u']
    if c in vogais:
        return True
    else:
        return False
c=input()
resultado=vogais(c)
print(resultado)

