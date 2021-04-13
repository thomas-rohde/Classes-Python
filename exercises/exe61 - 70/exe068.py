print('-' * 40)
print('{: ^40}'.format('LOJA LEO PUTA CUZÃO'))
print('-' * 40)
t = x = p0 = 0
b = ''
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    c = str(input('Quer continuar [ S / N ]: ')).strip().upper()[0]
    t += p
    if p0 == 0:
        b = n
        p0 = p
    elif p0 > p:
        b = n
        p0 = n
    if p >= 1000:
        x += 1
    if c == 'N':
        break
print('{:-^40}'.format('FIM DESSA POURRA!'))
print(f'''O total de compra foi R${t}
Temos {x} produtos custando acima de R$1000.00
O produto mais barato foi  {b} que custa R${p0}''')