d = int(input('Quantos dias você alugou o carro? '))
print('-' * 100)
km = float(input('Qual a distância percorrida com o carro? '))
t = float (60 * d) + (0.15 * km)

print('O carro que você alugou por {} dias, percorrendo {}Km, teve, no total, o preço de R${:.2f}'.format(d, km, t))