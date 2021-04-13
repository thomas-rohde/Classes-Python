m = float(input('Qual é seu massa (Kg)? '))
h = float(input('Qual é a sua altura (m)? '))
imc = m / h ** 2
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    t = str('ABAIXO DO PESO')
elif imc < 25:
    t = str('PESO IDEAL')
elif imc <= 30:
    t = str('SOBREPESO')
elif imc <= 40:
    t = str('OBESIDADE')
else:
    t = str('OBESIDADE MÓRBIDA')
print('\033[7m{}\033[m'.format(t))