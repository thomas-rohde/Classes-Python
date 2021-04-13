n = int(input('Insira um nº: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('''Analisando o número {}, teremos:
Unidade: {}
Dezena: {}
Centena : {}
Milhar: {}'''
.format(n, u, d, c, m))