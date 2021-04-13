n0 = int(input('Digite um nº '))
n1 = int(input('Digite outro nº '))
n2 = int(input('Só mais um, vai '))
#menor
m = n0
if n1<n0 and n1<n2:
    m = n1
if n2<n0 and n2<n1:
    m = n2
#MAIOR
m0 = n0
if n1>n0 and n1>n2:
    m0 = n1
if n2>n0 and n2>n1:
    m0 = n2
#Texto
print('O maior valor digitado foi {}'.format(m0))
print('O menor valor digitado foi {}'.format(m))