termo = int(input('Digite o termo da progressão aritmética: '))
p = int(input('Digite a razão: '))
tentativas = 11
adicionais = 0
while tentativas > 1:
    termo += p
    tentativas -= 1
    print(termo, end=', ')
adicionais = (int(input('\nDeseja digitar mais quantos termos? ')))
while adicionais > 0:
    a = adicionais + 1
    if a > 0:
        while a > 1:
            termo += p
            a -= 1
            print(termo, end=', ')
        adicionais = (int(input('\nDeseja digitar mais quantos termos? ')))
    else:
        print('\nFim do programa')
print('Assim encerramos!') 