s = float(input('Qual o salário do funcionário? R$'))
if s>1250:
    s0 = s * 1.10
else:
    s0 = s * 1.15
print('O seu salário era R${:.2f}, e agora é R${:.2f}'.format(s, s0))
