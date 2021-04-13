#x = int(input('Digite o primeiro termo da progressão: '))
#r = int(input('Digite a razão: '))
#for s in range(0, 10):
#    print(x + r*s, ' ', end='-> ')
#print('Acabou!')
x = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = x + (10 - 1) * r
for c in range(x, d, r):
    print('{} '.format(c), end='-> ')
print('Acabou')
