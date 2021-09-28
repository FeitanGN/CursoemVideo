from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
lista = (n1, n2, n3, n4, n5)
menor = maior = 0
if n1 > maior: maior = n1
if n2 > maior: maior = n2
if n3 > maior: maior = n3
if n4 > maior: maior = n4
if n5 > maior: maior = n5
if menor < n1: menor = n1
if n2 < menor: menor = n2
if n3 < menor: menor = n3
if n4 < menor: menor = n4
if n5 < menor: menor = n5
print('\033[32m+=-='*20, '\033[m')
print('Os números sorteados foram:\033[36m', end='')
for c in lista:
    print(c, end=' ')
print('\033[m')
print(f'O maior valor sorteado foi \033[31m{maior}\033[m.')
print(f'O menor valor sorteado foi \033[31m{menor}\033[m.')
print('\033[32m+=-='*20, '\033[m')
