n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
opt = 0
while opt != 5:
    print('''
Escolha a opção: 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] SAIR DO PROGRAMA''')
    opt = int(input('     SUA OPÇÃO: '))
    if opt == 1:
        print('A soma dos valores é \033[31m{}\033[m!'.format(n1 + n2))
        #opt = (int(input('Próximo comando: ')))
        print('-=-'*15)
    if opt == 2:
        print('A multiplicação dos valores é \033[31m{}\033[m!'.format(n1 * n2))
        #opt = (int(input('Próximo comando: ')))
        print('-=-'*15)
    if opt == 3:
        if n1 > n2:
            print('O maior número é \033[31m{}\033[m!'.format(n1))
            #opt = (int(input('Próximo comando: ')))
            print('-=-'*15)
        elif n1 == n2:
            print('Ambos possuem valores iguais.')
            #opt = (int(input('Próximo comando: ')))
            print('-=-'*15)
        else:
            print('O maior número é \033[31m{}\033[m!'.format(n2))
            #opt = (int(input('Próximo comando: ')))
            print('-=-'*15)
    if opt == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite o segundo valor: '))
        #opt = int(input('Sua opção: '))
    if opt > 5 or opt == 0:
        print('\033[31mComando inválido!\033[m')
        print('Tente novamente!')
        #opt = (int(input('Próximo comando: ')))
        print('-=-'*15)
    elif opt == 5:
        print('Fim do programa!')
        print('-=-'*15)
