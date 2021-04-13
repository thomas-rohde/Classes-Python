n = []
n0 = []
n1 = []
#Insira um valor
while True:
    n.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [s/n] '))
    if r in 'Nn':
        break
#Separação PAR / ÍMPAR
for c in n:
    if c % 2 == 0:
        n0.append(c)
    else:
        n1.append(c)
print(f'''A lista completa é {n}
A lista dos pares é {n0}
A lista dos ímpares é {n1}''')