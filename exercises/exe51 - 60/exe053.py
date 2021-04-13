ma = 0
me = 0
for p in range(1, 6):
    m = float(input('Massa da {}ª pessoa: '.format(p)))
    if p == 1:
        me = m
        ma = m
    else:
        if m > ma:
           ma = m
        if m < me:
            me = m
print('Analisando a massa dessas 5 pessoas, {}Kg foi o maior e {}Kg o menor'.format(ma, me))