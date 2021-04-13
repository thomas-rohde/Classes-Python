n0 = float(input('Primeira nota: '))
n1 = float(input('Segunda nota: '))
m = (n0 + n1) / 2
print('A média das notas {} e {} dá {}'.format(n0, n1, m))
if m >= 7:
    print('Parábens, você foi APROVADO!')
elif m <= 4:
    print('Você foi REPROVADO')
else:
    print('Você está de RECUPERAÇÃO!')