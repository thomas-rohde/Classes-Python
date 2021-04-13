s = str(' ')
while s not in 'MmFf':
    s = str(input('Informe o seu sexo[M/F]: ')).strip().upper()
    if s not in 'MmFf':
        print('Não aceito por ser LGBTfóbico, tente novamente')
print('Dados Validos, parábens')
