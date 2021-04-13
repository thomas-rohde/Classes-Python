n0 = int(input('Primeiro nº: '))
n1 = int(input('Segundo nº:  '))

if n0 > n1:
    print('O \033[7;36mPRIMEIRO\033[m número é maior')
elif n1 > n0:
    print('O \033[7;34mSEGUNDO\033[m número é maior  ')
else:
    print('\033[4;31mAMBOS\033[m os valores são iguais')
