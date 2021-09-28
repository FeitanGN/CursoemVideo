v = int(input('Qual a velociade do carro? '))
if v<=80:
        print('Tudo certo!')
else:
    print('Você recebeu uma multa de R${:.2f}'.format((v-80)*7))    