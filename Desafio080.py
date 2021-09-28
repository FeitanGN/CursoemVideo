lista = []
maior = menor = 0
print('\033[32m+++'*20, '\033[m')
for n in range(0, 5):
    x = int(input('Digite um número: '))
    if n == 0:
        maior = menor = x
        print('Adicionado no final da lista.')
        lista.append(x)
    if n == 1:
        if x >= maior:
            lista.append(x)
            print('Adicionado no final da lista.')
            maior = x
        else:
            lista.insert(0, x)
            print('Adicionado no início da lista.')
            menor = x
    if n == 2:
        if x >= maior:
            lista.append(x)
            print('Adicionado no final da lista.')
            maior = x
        elif x <= menor:
            lista.insert(0, x)
            print('Adicionado no início da lista.')
            menor = x
        else:
            lista.insert(1, x)
            print('Adicionado no meio da lista.')
    if n == 3:
        if x >= maior:
            lista.append(x)
            print('Adicionado no final da lista.')
            maior = x
        elif x <= menor:
            lista.insert(0, x)
            print('Adicionado no início da lista.')
            menor = x
        elif x >= lista[1]:
            lista.insert(2, x)
        else:
            lista.insert(1, x)
            print('Adicionado no meio da lista.')
    if n == 4:
        if x >= maior:
            lista.append(x)
            print('Adicionado no final da lista.')
            maior = x
        elif x <= menor:
            lista.insert(0, x)
            print('Adicionado no início da lista.')
            menor = x
        elif x <= lista[1]:
            lista.insert(1, x)
            print('Adicionado no meio da lista.')
        elif x < lista[2]:
            lista.insert(2, x)
            print('Adicionado no meio da lista.')
        else:
            lista.insert(2, x) if x <= lista[2] else lista.insert(3, x)
            print('Adicionado no meio da lista.')
print('\033[32m+++'*20, '\033[m')
print(f'Os valores digitados em ordem ficaram assim: {lista}.')
print('\033[32m+++'*20, '\033[m')
