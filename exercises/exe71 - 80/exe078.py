#nu = []
#i = n0 = n1 = n2 = n3 = n4 = 0
#for c in range(0, 5):
#    n = int(input('Digite um valor: '))
#    if c == 0:
#        n0 = n1 = n2 = n3 = n4 = n
#        i = 0
#   elif n < n0:
#       i = 0
#        n0 = n
#    elif n < n1:
#        i = 1
#       n1 = n
#    elif n < n2:
#        i = 2
#        n2 = n
#    elif n < n3:
#        i = 3
#        n3 = n
#    elif n < n4:
#        i = 4
#        n4 = n
#    elif n > n4:
#        i = 4
#       n4 = n
#   if n == n4:
#       print('Adicionado ao final da lista')
#    else:
#        print(f'Adicionado a posição {i} da lista...')
#    nu.insert(i, n)
#print('-' * 30)
#print(f'Os valores digitados em formato crescente foi {nu}')
num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da fila')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores foram, em ordem crescente: {num}')