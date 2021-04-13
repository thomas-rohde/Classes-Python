from random import randint
from time import sleep
print('-'*30)
d = int(input('Eu escolho um número entre 0 e 5, tente adivinhar qual: '))
print('-'*30)
f = int(randint(0, 5))
print('PROCESSANDO...')
sleep(2)
if f == d:
    print('Parabéns, você vençeu')
else:
    print('Que pena, você perdeu, eu escolhi {}'.format(f))