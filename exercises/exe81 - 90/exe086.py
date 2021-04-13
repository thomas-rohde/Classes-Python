matriz = [[], [], []]
r = list(range(0, 3))
spar = v3c = m2 = 0
for c in r:
    for i in r:
        matriz[c].append(int(input(f'Digite um valor para[{c}, {i}]: ')))
print('-' * 40)
for d in r:
    print('  (', end=' ')
    for j in r:
        dj = matriz[d][j]
        print(f'[{dj:^8}]', end=' ')
        if dj % 2 == 0:
            spar += dj
        if j == 2:
            v3c += dj
        if d == 1 and j == 0:
            m2 = dj
        elif d == 1 and m2 < dj:
            m2 = dj
    print(')')
print('-' * 40)
print(f'''A soma dos nºs pares dá {spar},
enquanto a soma dos valores da 3ª coluna é {v3c}.
E por fim, o maior nº da 2ª linha é {m2}\n''',
'-' * 40)