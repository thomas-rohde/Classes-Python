from datetime import date
a = int(input('Qual o seu ano de nascimento? '))
a0 = date.today().year
i = a0 - a
print('Quem nasceu em {} tem / vai fazer {} em {}'.format(a, i, a0))
if i == 18:
    print('Você deve se alistar \033[4:31mIMEDIATAMENTE\033[m')
elif i > 18:
    print('Você deveria ter se alistado faz {} ano(s)'.format(i - 18))
else:
    print('Você não pode se alistar, espere mais {} ano(s)'.format(18 - i))
