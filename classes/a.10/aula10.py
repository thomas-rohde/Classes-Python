#nome = str(input('Qual é o seu nome? '))
#if nome == 'Thomas':
#    print('Que nome lindo você tem')
#else:
#    print('Já vi nome melhor')
#print('Tenha um bom dia {}'.format(nome))
n0 = float(input('Qual foi a sua 1ª nota? '))
n1 = float(input('Qual foi a sua 2ª nota? '))
n = (n0 + n1) / 2
print (('Parábens, você passou de ano! Com {}'.format(n)) if n >= 6 else ('Você ficou de recuperação, estude'))