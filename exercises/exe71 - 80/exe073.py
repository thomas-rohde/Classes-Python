n9 = par = 0
n = (int(input('Digite um nº: ')), int(input('Digite um nº: ')), int(input('Digite um nº: ')),
    int(input('Digite um nº: ')), int(input('Digite um nº: ')))
for n0 in n:
    if n0 == 9:
        n9 += 1
    elif n0 % 2 == 0:
        par += 1
print(f'''Você digitou {sorted(n)}
O valor 9 apareceu {n.count(9)} vezes''')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1} posição')
else:
    print('3 encontrado em nenhuma posição')
print(f'Os valores pares digitados  foram {par}, e eles foram ', end='')
for n0 in n:
    if n0 % 2 == 0:
        print(n0, '- ', end='')
print('FIM!')