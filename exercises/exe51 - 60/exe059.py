print('Gerador de PA\n', '-=' * 8)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
while c != 10:
    c += 1
    print('{} -> '.format(pt), end='')
    pt += r
print('FIM')