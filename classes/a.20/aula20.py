def linha():
    print('-' * 30)


def mensagem(txt):
    print('-=-' * 10)
    print(txt)
    print('-=-' * 10)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')


# PROGRAMA PRINCIPAL
linha()
mensagem(f'''{'Se goxxxta n goxxxta?':^30}''')
soma(8, 4)
linha()
soma(b=3, a=1)


def contando(*num):
    for c in num:
        print(f'{c} - ', end='')
    print(f'temos, no total, {len(num)} valores')


contando(1, 2, 3, 4, 7)
contando(999, 5)
contando(4, 6, 7, 5)