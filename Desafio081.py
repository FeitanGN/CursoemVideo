lista = []
r = 'S'
print('\033[32m***'*20, '\033[m')
while r == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar?\033[35m[S/N]\033[m ')).strip().upper() [0]
    while r not in 'NS':
        print('\033[31mDigite novamente!\033[m')
        r = str(input('Deseja continuar?\033[35m[S/N]\033[m ')).strip().upper() [0]
    if r == 'N':
        break
print('\033[32m***'*20, '\033[m')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')
print('\033[32m***'*20, '\033[m')
