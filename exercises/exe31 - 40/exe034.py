v = float(input('Qual o valor da casa? R$'))
t = int(input('Em quanto tempo você deseja pagar? '))
s = float(input('Quanto é o seu salário?'))
a = (v / (12 * t))


if a <= (0.3 * s):
    print(f'''\033[4;32mParábens! Você conseguiu o financiamento,\033[m
    As parcelas serão de R${a:.2f}, para se pagar a casa de R${v:.2f} em {t} anos''')
else:
    print('Empréstimo \033[4;31mNEGADO\033[m')