lista = []
print('\033[32m+++'*20, '\033[m')
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} a lista')
                break
            pos += 1
print('\033[32m+++'*20, '\033[m')
print(f'Os valores digitados em ordem são: {lista}')
print('\033[32m+++'*20, '\033[m')