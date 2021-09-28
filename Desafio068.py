from random import randint
print('\033[32m-='*20)
print('Vamos jogar par ou ímpar')
print('-='*20, '\033[m')
cont = 0
while True:
    c = randint(0, 10)
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? \033[31m[P/I]\033[m ')).strip().upper() [0]
    while escolha not in 'PN':
        escolha = str(input('Par ou ímpar? \033[31m[P/I]\033[m ')).strip().upper() [0]
    soma = c + n
    cont += 1
    if soma % 2 == 0:
        if escolha == 'P' :
            print('Parabéns, par, você acertou!')
        elif escolha == 'I':
            print('\033[31mVocê Perdeu!\033[m')
            break
    elif soma % 2 == 1:
        if escolha == 'I' :
            print('Parabéns, par, você acertou!')
        elif escolha == 'P':
            print('\033[31mVocê Perdeu!\033[m')
            break
print('\033[32m-='*20, '\033[m')
print(f'\033[31mVocê jogou {n} e o computador {c} somando {soma}!\033[m')
print('Jogo encerrado. Você jogou {} vezes.'.format(cont))
print('\033[32m-='*20, '\033[m')