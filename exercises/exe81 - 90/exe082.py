#eq = str(input('Digite a expressão: '))
#x1 = eq.count('(')
#x2 = eq.count(')')
#if x1 == x2:
#    print('Essa equação é real')
#else:
#    print('Essa equação é falsa')
eq = str(input('Digite a expressão: '))
paren = []
for simb in eq:
    if simb == '(':
        paren.append('(')
    elif simb == ')':
        if len(paren) > 0:
            paren.pop()
if len(paren) == 0:
    print('Essa equação é verdadeira')
else:
    print('Essa equação é falsa')