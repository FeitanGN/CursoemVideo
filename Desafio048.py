from typing import final


#Soma, impares, divisíveis por 3 até 500
print('+++'*10, 'Iniciando o programa..', '+++'*10)
p = 0
for f in range(1, 500):
    if f % 3 == 0 and f % 2 != 0:
        p += f
print('A soma dos números ímpares divisíveis por 3 é {}.'.format(p))
