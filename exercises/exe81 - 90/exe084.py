nu = [[], []]
n = 0
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        nu[0].append(n)
    else:
        nu[1].append(n)
nu[0].sort()
nu[1].sort()
print(f'''A lista par é {nu[0]},
Enquanto a lista ímpar é {nu[1]}''')