pessoa = dict()
pessoas = []
cdade = media = 0
while True:
    pessoa['nome:'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
        if pessoa['sexo'] not in 'MmFf':
            print('Erro, dado não aceito por lgbtfobia, tente novamente')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    cdade += pessoa['idade']
    pessoa.clear()
    while True:
        r = str(input('Quer continuar? [s/n] '))
        if r not in 'SsNn':
            print('ERRO! Tente novamente colocando S/N')
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
media = cdade / len(pessoas)
print(f'Ao todo, temos {len(pessoas)} pessoas cadastradas.\nA média de idade é {media}.\n'
      f'As mulheres cadastradas foram: ')
for c in pessoas:
    if c['sexo'] in 'Ff':
        print(f'{c["nome"]}', end='  ')
print('\nLista de pessoas que estão acima da média: ', end='')
for c in pessoas:
    if media < c['idade']:
        print(' ' * 5)
        for k, v in c.items():
            print(f'{k} = {v}', end='')