print('\033[34m+++'*20, '\033[m')
lista = ((int(input('Digite um número: '))),
        (int(input('Digite um número: '))),
        (int(input('Digite um número: '))), 
        (int(input('Digite um número: '))))
print('\033[34m+++'*20, '\033[m')
par = 0
print('\033[32m+++'*20, '\033[m')
if 9 in lista:
    print(f'O valor 9 apareceu {lista.count(9)} vezes.')
else:
    print('Nenhum 9 foi digitado.')
for c in range(0, len(lista)):
    if lista[c] == 3:
        print(f'O valor 3 aparece primeiro na {c + 1}ª posição ')
        break
if 3 not in lista:
    print('Nenhum 3 foi digitado')
print('Os números pares digitados são: ', end='')
for p in range(0, len(lista)):
    if lista[p] % 2 == 0:
        par += 1
        print(lista[p], end=' ')
print(f'\nSão {par} ao todo')
print('A tupla é:',  lista)
print('\033[32m+++'*20, '\033[m')

