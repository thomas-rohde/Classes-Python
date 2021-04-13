print('=' * 30)
print('{: ^.30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)
v = int(input('Que valor você quer sacar? '))
print('-' * 30)
c = 50
x = 0
while True:
    if v >= c:
        x += 1
        v -= c
        if v < c and x > 0:
            print(f'Total de {x} cédulas de R${c}')
    else:
        if v >= 20:
            c = 20
            x = 0
        elif v >= 10:
            c = 10
            x = 0
        elif v >= 1:
            c = 1
            x = 0
        else:
            break
print('-' * 30)
print('Volte sempre!')