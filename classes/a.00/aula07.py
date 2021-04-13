n1 = int(input('Digite um nº:'))
n2 = int(input('Digite outro nº:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
p = n1 ** n2
r = n1 ** (1/n2)
print(f'A soma é {s:~<5}. A multiplicação é {m:=>5}. A divisão é {d:°^5}, enquanto a divisão inteira é {di}, com resto {dr}.')
print ('A elevação é {}, enquanto a raiz é {:.3f}' .format(p, r))