from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
dados['idade'] = datetime.now().year - anonasc
if dados['ctps'] != 0:
    anocont = int(input('Ano de Contratação: '))
    dados['contratação'] = datetime.now().year - anocont
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = (dados["contratação"] + 35)
print('-=-' * 30)
for k, v in dados.items():
    print(f'{k} tem valor: {v}')