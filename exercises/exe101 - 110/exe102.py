def ficha(nome='<desconhecido>', n=0):
    print(f'O jogador {nome} fez {n} gol(s) no campeonato')


#MAIN
nome0 = str(input('Nome do Jogador: '))
n0 = str(input('Nº de gols: '))
if n0.isnumeric():
    n0 = int(n0)
else:
    n0 = 0
if nome0.strip() == '':
    ficha(n=n0)
else:
    ficha(nome0, n0)