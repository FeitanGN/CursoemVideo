from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
print('-=-' * 30)
player = str(input('Escolha sua mão: ')).strip().lower()
print('++'*10, 'Jo', '++'*10), sleep(1)
print('++'*10, 'Ken', '++'*10), sleep(1)
print('++'*10, 'po!!', '++'*10), sleep(1)
print('-=-' * 30)
if player != 'pedra' and player != 'papel' and player != 'tesoura':
    print('Valor inválido!')
elif player == pc:
    print('\033[1;33mEmpate\033[m.') 
    print('Você escolheu \033[7m{}\033[m e o computador \033[7m{}\033[m!'.format(player, pc))
elif player != pc:
    #print(str('o'*20, player, 'x', pc, 'o'*20).upper())
    if player == 'pedra' and pc == 'papel':
        print('\033[1;31mPerdeu!\033[m Você escolheu \033[7m{}\033[m e o computador \033[7m{}\033[m!'.format(player, pc))
    elif player == 'papel' and pc == 'tesoura':
        print('\033[1;31mPerdeu!\033[m Você escolheu \033[7m{}\033[m e o computador \033[7m{}\033[m!'.format(player, pc))
    elif player == 'tesoura' and pc == 'pedra':
        print('\033[1;31mPerdeu!\033[m Você escolheu \033[7m{}\033[m e o computador \033[7m{}\033[m!'.format(player, pc))
    else:
        print('\033[1;32mVocê venceu.\033[m Você escolheu \033[7m{}\033[m e o computador \033[7m{}\033[m!'.format(player, pc))
print('-=-' * 30)