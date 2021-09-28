s = float(input('Qual é seu salário? ')) 
if s > 1250:
    print('Você teve um aumento de 10%, assim seu novo salário é R$ {:.2f}!'.format((s*0.1)+s))
else:
    print('Você teve um aumento de 15%, assim seu novo salário é R$ {:.2f}!'.format((s*0.15)+s))
