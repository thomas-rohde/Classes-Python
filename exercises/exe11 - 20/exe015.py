'''Calcula a hip com base em pit'''

'''from math import sqrt, pow
print('Digite os lados do triângulo retangulo:')
print('-' * 39)
l0 = float(input('Digite o 1º lado(co): '))
l1 = float(input('Digite o 2º lado(ca): '))

print('-' * 39)
print('O traiângulo formado tem como hipotenusa:\n{:.2f}'.format(sqrt(pow(l0, 2) + pow(l1, 2))))'''

from math import hypot
l0 = float(input('Digite o Cateto Adjacente: '))
l1 = float(input('Digite o Cateto Oposto: '))
print('A Hipotenusa desse triângulo é {:.2f}'.format(hypot(l0, l1)))