n = int(input('Digite um nº e veremos se ele é primo! '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
        print('\033[7;31m{}\033[m'.format(c), end=' ')
    else:
        print('\033[4;32m{}\033[m'.format(c), end=' ')
if s == 2:
    print('\nEste nº é primo!')
else:
    print('\nEste nº não é primo, é divisivel por {} nºs'.format(s))