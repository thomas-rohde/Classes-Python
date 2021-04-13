from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
ppt = int(input('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
t = randint(0, 2)
print('''{:=^20}
Jogador Escolheu: [{}]
Computador Escolheu: [{}]
{:=^20}'''.format(' JO - KEM - PÔ ', itens[ppt], itens[t], ' JO - KEM - PÔ '))
if t == 0: #computador jogou PEDRA
    if ppt == 0:
        print('Empate')
    elif ppt == 1:
        print('Jogador vence!')
    else:
        print('Computador venceu!')
elif t == 1: #computador jogou PAPEL
    if ppt == 0:
        print('Computador venceu!')
    elif ppt == 1:
        print('Empate')
    else:
        print('Jogador venceu!')
else: #computador jogou TESOURA
    if ppt == 0:
        print('Jogador venceu!')
    elif ppt == 1:
        print('Computador venceu!')
    else:
        print('Empate')