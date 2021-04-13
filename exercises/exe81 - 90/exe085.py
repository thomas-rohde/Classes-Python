matriz = [[], [], []]
R = list(range(0, 3))
for c in R:
    for i in R:
        matriz[c].append(int(input(f'Digite um valor para[{c}, {i}]: ')))
print('-' * 30)
for d in R:
    print('(', end=' ')
    for j in r:
        print(f'[{matriz[d][j]:^5}]', end=' ')
    print(')')