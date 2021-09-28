print('\033[32m###'*15, '\033[m')
lista = []
for n, v in enumerate(range(0, 5)):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
print('\033[32m---'*15, '\033[m')
print(f'Você digitou : {lista}')
print(f'O maior digitado foi {max(lista)} nas posições ', end='')
for c, v in enumerate(lista):
    if v == max(lista):
        print(c, end=',')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ',end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(c, end=',')
print('\n', '\033[32m###'*15, '\033[m')
