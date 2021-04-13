from datetime import date
a = date.today().year
i = int(input('Ano de Nascimento: '))
e = a - i
if e > 25:
    print('Você é da categoria MASTER')
elif 19 <= e < 26:
    print('Você é da categoria SÊNIOR')
elif 15 < e <= 18:
    print('Você é da categoria JÚNIOR')
elif 9 < e <= 14:
    print('Você é da categoria INFANTIL')
else:
    print('Você é da categoria MIRIM')