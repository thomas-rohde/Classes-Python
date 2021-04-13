from random import choice
n0 = input('Escreva o nome da 1ªaluna: ')
n1 = input('Escreva o nome da 2ªaluna: ')
n2 = input('Escreva o nome da 3ªaluna: ')
n3 = input('Escreva o nome da 4ªaluna: ')
lista = [n0, n1, n2, n3]

print('A aluna sorteada foi {}'.format(choice(lista)))