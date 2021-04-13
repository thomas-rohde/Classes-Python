time = []
jogador = []
dados = {}
while True:
    dados.clear()
    jogador.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    t = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(0, t):
        jogador.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    dados['Gols'] = jogador[:]
    dados['Total'] = sum(jogador)
    time.append(dados.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Dado inválido, tente novamente')
    if r == 'N':
        break
print('-=-' * 15)
print('cod', end=' ')
for i in dados.keys():
    print(f'{i:<15}', end='')
print('\n', '-' * 45)
for k, v in enumerate(time):
    print(f'{(k + 1):>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? [0 finaliza] '))
    if busca == 0:
        break
    if busca >= len(time):
        print('ERRO! Tente novamente')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for w, y in enumerate(time[busca]['Gols']):
            print(f' Na partida {w + 1}, {time[busca]["Nome"]} fez {y} gols')
    print('-' * 45)