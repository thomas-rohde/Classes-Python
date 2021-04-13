from math import factorial
fac = int(input('Escolha um nº: '))
f = fac
print('Calculando {}!'.format(fac))
while f != 0:
    print('{}'.format(f), end='')
    print(' x ' if f > 1 else ' = ', end='')
    f -= 1
print(factorial(fac))
