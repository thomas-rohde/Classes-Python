v = float(input('Insira a velocidade do carro, em Km/h: '))
a = ((v - 80)*7)
if v <= 80:
    print('Tudo nos conformes')
else:
    print('Deverá pagar uma multa por andar a {}Km/h de R${:.2f}'.format(v, a))