n = 0
n0 = 0
n1 = int(input('Digite um nº (999 cancela a contagem): '))
while n1 != 999:
    n0 += n1
    n += 1
    n1 = int(input('Digite um nº (999 cancela a contagem): '))
print('A soma desses {} nºs deu {}'.format(n, n0))
