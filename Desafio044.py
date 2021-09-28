print('{:=^40}'.format('LOJAS DO IRNAB'))
p = float(input('Qual o preço do poduto? '))
print('Escolha a condição de pagamento:')
print('[ 1 ] à vista(dinheiro ou cheque)(10% de desconto)')
print('[ 2 ] à vista no cartão          (5% de desconto)')
print('[ 3 ] 2x no cartão               (preço normal)')
print('[ 4 ] 3x ou mais no cartão       (20% de juros)')
cond = int(input('Qual a condição de pagamento?'))
if cond==1:
    print('O preço com desconto fica \033[1;32mR$ {:.2f}\033[m!'.format(p*0.9))
elif cond==2:
    print('O preço com desconto fica \033[1;32mR$ {:.2f}\033[m!'.format(p*0.95))
elif cond==3:
    print('O preço fica \033[1;32mR$ {:.2f}\033[m! em duas parcelas de R$ {:.2f} sem juros' .format(p, p/2))
elif cond==4:
    parc = int(input('Em quantas parcelas? '))
    novas = p * 1.2 / parc
    print('O preço com juros fica \033[1;32mR$ {:.2f}\033[m! em {} parcelas de R$ {:.2f} com 20% de juros.'.format(p*1.2, parc, novas))
else:
    print('Número não reconhecido!')
