n1 = 0
n2 = 1
quantidade = int(input('Quantos termos você quer mostrar? '))
x = 0
n3 = 0
print('{} -> {} -> '.format(n1, n2), end='')
while x != quantidade - 2:
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    n1 = n2
    n2 = n3
    x += 1
print('Fim!')
