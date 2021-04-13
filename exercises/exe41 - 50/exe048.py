s = 0
for par in range(0, 6):
    q = int(input('Digite um valor:'))
    if q % 2 == 0:
        s+= q
print(s)