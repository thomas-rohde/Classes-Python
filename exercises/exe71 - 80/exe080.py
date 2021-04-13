num = []
n = 0
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip()
    n += 1
    if r in 'Nn':
        break
num.sort(reverse=True)
print(f'''Você digitou {n} elementos.
Os valores digitados foram, em orfdem decrescente {num}''')
if 5 in num:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')