from random import shuffle
n0 = input('1ª Aluna: ')
n1 = input('2ª Aluna: ')
n2 = input('3ª Aluna: ')
n3 = input('4ª Aluna: ')
l = [n0, n1, n2, n3]
shuffle(l)

print('A ordem dos alunos é {}'.format(l))