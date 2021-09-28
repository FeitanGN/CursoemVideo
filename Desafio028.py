from time import sleep
from random import randint
n = int(randint(0,5))
e = int(input('Adivinhe um número de 0 a 5: '))
print('Aguarde, processando...') 
sleep(3) #em segundos
if n == e:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número era {}. Tente novamente!'.format(n))   
