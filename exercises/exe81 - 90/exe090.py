from random import randint
from time import sleep
from  operator import itemgetter
jogo = {}
ranking = {}
print('{:-^50}'.format('JOGANDO DADOS'))
for c in range(1, 5):
    jogo[f"jogador {c}"] = randint(1, 6)
for k, v in jogo.items():
    sleep(0.7)
    print(f'{k} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('{:-^50}'.format('Calculando a ordem'))
for k0, v0 in enumerate(ranking):
    sleep(0.7)
    print(f'{k0 + 1}º Lugar: {v0}')
    print(f'-' * 50)