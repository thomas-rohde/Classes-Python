n0 = ''
i0 = 0
mi = 0
f20 = 0
for p in range(1, 5):
    print('-' * 6, '{}ª PESSOA'.format(p), '-' * 6)
    n = str(input('Nome: ')).strip().capitalize()
    i = int(input('Idade: '))
    s = str(input('Sexo [M / F]: ')).strip().upper()
    mi += i
    if p == 1:
        i0 = i
    if i0 < i and s == 'M':
        n0 = n
        i0 = i
    elif i < 20 and s == 'F':
        f20 += 1
print('''Essas pessoas tem, em média, {} anos.
Sendo o homem mais velho {}, com {} anos.
E há {} pessoas do sexo feminino com menos de 20 anos'''.format(mi // 4, n0, i0, f20))