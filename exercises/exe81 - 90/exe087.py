from random import randint
from time import sleep
megasena = []
count = 0
p = 'Processando...'
r = int(input('Quantos jogos você quer que eu sorteie? ')) + 1
for c in range(1, r):
    while len(megasena) < 6:
        n = randint(1, 60)
        if n not in megasena:
            megasena.append(n)
    print(f'{p:-^30}')
    sleep(1.2)
    print(f'Jogo {c}: {megasena}')
    megasena.clear()
p = 'BOA SORTE!'
print('-' * 30 ,'\n     Processo Finalizado!')
print(f'{p:-^30}')