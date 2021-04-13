maracana = []
dados = {}
dados['Nome'] = str(input('Nome: '))
t = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, t):
    maracana.append(int(input(f'Quantos gols na partida {c}? ')))

dados['Gols'] = maracana[:]
dados['Total'] = sum(maracana)
print('=' * 45, '\n', dados)
print('-=-' * 15)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 15)
for i, v in enumerate(dados['Gols']):
    print(f'Na partida {i}, fez um total de {v} gols.')
print(f'Foi um total de {dados["Total"]}')
print('-=-' * 15)

