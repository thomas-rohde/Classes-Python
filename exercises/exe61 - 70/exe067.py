c = ''
m = s0 = f20 = 0
print('=' * 22)
print('Cadastrador de Pessoas')
print('=' * 22)
while c == 'N':
    i = int(input('Idade: '))
    s = str(input('Sexo [ M / F ]: ')).strip().upper()[0]
    print('-' * 22)
    if i >= 18:
        m += 1
    if s == 'M':
        s0 += 1
    elif i < 20 and s == 'F':
        f20 += 1
    c = str(input('Quer continuar [ S / N ]? ')).strip().upper()[0]
    print('-' * 22)
print(f'''O total de pessoas com 18 anos ou mais são {m}
Ao total temos {s0} homens
E temos {f20} mulheres abaixo de 20 anos''')
