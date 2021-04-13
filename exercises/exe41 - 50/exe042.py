#print('========== LOJAS COMUNA ==========')
print('{:=^40}'.format('LOJAS COMUNA'))
p = float(input('Preço das compras: R$'))
f = int(input('''FORMAS DE PAGAMENTO
\033[7m[ 1 ] à vista dinheiro / cheque\033[m
\033[7;31m[ 2 ] à vista no cartão\033[m
\033[7;32m[ 3 ] 2x no cartão\033[m
\033[7;34m[ 4 ] 3x ou mais no cartão\033[m
\033[4mQual é a opção?\033[m '''))
if f == 1:
    print('O preço de se pagar a vista com dinheiro / cheque R${:.2f}'.format(p * 0.9))
elif f == 2:
   print('O preço de se pagar a vista com cartão R${:.2f}'.format(p * 0.95))
elif f == 3:
    print('O preço é de R${:.2f} dividido em duas parcelas de R${:.2f}'.format(p, p / 2))
elif f == 4:
    x = int(input('Em quantas vezes deseja pagar?'))
    v =f * 1.2
    if x == 2:
        print('O preço é de R${:.2f} dividido em duas parcelas de R${:.2f}'.format(p, p / 2))
    elif x == 1:
        print('O preço de se pagar a vista com cartão R${:.2f}'.format(p * 0.95))
    print('O preço, com juros é R${:.2f} pagando em três vezes ou mais é de R${:.2f}'.format(v, v / x))
else:
    print('Solução não pode ser aceita, tente novamente')