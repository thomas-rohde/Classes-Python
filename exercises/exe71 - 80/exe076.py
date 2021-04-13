n = []
i = n0 = n1 = 0
for i in range(0, 5):
    n.append(int(input(f'Digite um valor para a Posição {i}: ')))
    if i == 0:
        n0 = n1 = n[i]
    else:
        if n0 > n[i]:
            n0 = n[i]
        if n1 < n[i]:
            n1 = n[i]

print('-' * 30)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {n1} nas posições', end=' ')
for i0, i1 in enumerate(n):
    if i1 == n1:
        print(f'{i0}...', end='')
print(f'\nO menor valor digitado foi {n0} na posição', end=' ')
for i0, i1 in enumerate(n):
    if i1 == n0:
        print(f'{i0}...', end='')
