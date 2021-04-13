s = int(input('Digite a distância que deseja percorrer (em Km): '))
'''if s <= 200:
    print('Sua viajem então custará R${:.2f}'.format(0.5 * s))
else:
    print('Sua viajem irá custar R${:.2f}'.format(0.45 * s))
print('-Boa Viajem!-' * 5)'''
preço = s * 0.5 if s <= 200 else s * 0.45
print('Sua viajem vai custar R${:.2f}. Boa viajem!'.format(preço))