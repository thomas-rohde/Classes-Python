print('Gerador de PA (Advanced)')
print('-=' * 8)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 10
count = 0
while c != 0:
    d = c
    while d != 0:
        count += 1
        d -= 1
        print('{} -> '.format(pt), end='')
        pt += r
    print('PAUSA')
    c = int(input('Quantos termos a mais você quer? '))
print('Programa finalizado com {} termos da PA contados, tenha um bom dia!'.format(count))