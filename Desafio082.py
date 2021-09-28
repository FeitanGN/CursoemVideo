lista = []
par = []
impar = []
r = 'S'
print('\033[32m-='*30, '\033[m')
while r == 'S':
    x = (int(input('\033[34mDigite um número: \033[m')))
    lista.append(x)
    r = input('Deseja continuar?\033[35m[S/N]\033[m ').upper().strip() [0]
    while r not in 'NS':
        print('\033[31mValor errado, digite novamente!\033[m')
        r = input('Deseja continuar?\033[35m[S/N]\033[m ').upper().strip() [0]
    if r == 'N':
        break
for tipo in lista:
    if tipo % 2 == 0:
        par.append(tipo)
    else:
        impar.append(tipo)
print('\033[32m-='*30, '\033[m')
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
print('\033[32m-='*30, '\033[m')