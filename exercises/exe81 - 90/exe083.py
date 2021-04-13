pessoas = []
grupo = []
c = mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Idade: ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    r = str(input('Quer continuar? [s/n] ')).strip()
    if r in 'Nn':
        break
for c, pessoa in enumerate(grupo):
    if c == 0:
        mai = men = pessoa[1]
    elif mai < pessoa[1]:
        mai = pessoa[1]
    elif men > pessoa[1]:
        men = pessoa[1]
print(f'Ao todo, você cadastrou {c + 1} pessoas.')
print(f'As pessoas mais velhas tem {mai} anos de idade, sendo elas', end=' ')
for p in grupo:
    if mai == p[1]:
        print(p[0], end=', ')
print(f'\nAs pessoas mais novas tem {men} anos de idade, sendo elas', end=' ')
for p in grupo:
    if men == p[1]:
        print(p[0], end=', ')