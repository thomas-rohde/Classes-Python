nome = str(input('Qual é o seu nome? ')).strip()

print('''O seu nome apenas em letras garrafais (porém amigáveis) é {}
Já em letras minusculas {}. Seu nome possuí {} letras.
Seu primeiro nome tem {} '''.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome tem {}'.format(len(separa[0])))