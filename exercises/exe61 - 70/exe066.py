from random import randint
y = c = 0
while True:
    n = int(input('Digite um nº: '))
    pi = str(input('Par ou Ímpar [ P / I ]: ')).strip().upper()[0]
    x = int(randint(0, 11))
    y = (x + n) % 2
    print('=' * 30)
    if (pi == 'Pp' and y == 0) or (pi == 'Ii' and y == 1):
        print(f'Você ganhou! Você jogou {n}, enquanto o computador jogou {x}')
    else:
        print('Você perdeu!')
        break
    c += 1
    print('=' * 30)
print('=' * 30)
print(f'Pela soma entre {n} e {x}, mas que pena. Você ganhou {c} vezes.')
