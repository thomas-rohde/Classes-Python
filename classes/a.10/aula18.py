#test = []
#test.append('Gustavo')
#test.append(40)
#guys = []
#guys.append(test[:])
#test[0] = 'Maria'
#test[1] = 22
#print(test, guys[0][1])
galera = list()
dado = []
for c in range(0, 5):
    dado.append(str(input('Qual é o seu nome? ')))
    dado. append(int(input('Qual é a sua idade?')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')