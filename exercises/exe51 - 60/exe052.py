from datetime import date
ma = me = 0
for c in range(1, 8):
    n = int(input('Em q ano {}ª pessoa nasceu? '.format(c)))
    if date.today().year - n >= 21:
        ma += 1
    else:
        me += 1
print('{} pessoas são da maioridade\n{} são da menoridade'.format(ma, me))