aluno = {}
aluno["Nome"] = str(input('Nome: '))
aluno["Média"] = float(input(f'Média  de {aluno["Nome"]}: '))
if aluno["Média"] >= 7:
    aluno["Situação"] = 'Aprovado'
else:
    aluno["Situação"] = 'Recuperação'
print('-' * 30)
for k, v in aluno.items():
    print(f' -> {k} da aluna é {v}')