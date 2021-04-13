nu = []
n = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in nu:
        nu.append(n)
    else:
        print('Valor já inserido')
    sn = str(input('Deseja continuar?[S/N] ')).strip()
    if sn in 'Nn':
        break
print(f'Você digitou os valores: {sorted(nu)}')