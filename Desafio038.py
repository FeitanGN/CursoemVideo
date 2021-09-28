n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1>n2:
    print('O número \033[1;33m{}\033[m é maior que o número \033[1;33m{}\033[m!'.format('primeiro valor', 'o segundo'))
elif n2>n1:
    print('O número \033[1;33m{}\033[m é maior que o número \033[1;33m{}\033[m!'.format('segundo valor', 'o primeiro'))
else:
    print('Não existe valor maior, ambos são iguais!')
