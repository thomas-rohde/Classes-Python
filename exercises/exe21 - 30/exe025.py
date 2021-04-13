n = str(input('Qual é o seu nome? '))
l = n.split()

print('''O nome {}
Tem como nome {}
e o último sobrenome {}'''
.format(n, l[0], l[len(l) - 1]))