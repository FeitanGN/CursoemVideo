#jogo de acertos
from random import randint
n = randint(1, 10)
tentativas = 1
escolha = int(input('Escolha um número de 1 a 10! '))
#escolha = false
#while not escolha
while n != escolha:
    print('\033[31mVocê errou, tente novamente!\033[m')
    escolha = int(input('Escolha um número de 1 a 10! '))
    #escolha = true
    tentativas += 1
print('=+'*20)
print('\033[32mVocê acertou, parabéns!\033[m')
print('Você precisou de \033[3;35m{}\033[m tentativas pra acertar.'.format(tentativas))
print('=+'*20)