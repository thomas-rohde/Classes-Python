#for c in range(0, 6, 2):
#    print('Oi')
i = int(input('Início:'))
p = int(input('Passo: '))
f = int(input('Fim: '))
s = 0
for c in range(i, f + 1, p):
    n = int(input('Digite um valor: '))
    s += n  #s = s + n#
print('A soma desses valores é {}'.format(s))