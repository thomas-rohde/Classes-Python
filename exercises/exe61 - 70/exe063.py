deseja = str('S')
n = x = n1 = n2 = m = 0
while deseja != 'N':
    n = int(input('Insira um nº: '))
    x += 1
    m += n
    if x == 1:
        n1 = n2 = n
    else:
        if n1 < n:
            n1 = n
        if n2 > n:
            n2 = n
    deseja = str(input('Deseja continuar? [S / N]')).strip().upper()[0]
print(' O maior nº foi {} enquanto o menor foi {}, tendo a média {}'.format(n1, n2, m / x))
