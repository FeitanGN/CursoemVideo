lista = []
r = 'S'
print('\033[36m***'*20, '\033[m')
while r == 'S':
    x = int(input('Digite um número: '))
    if x in lista:
        print('\033[31mNúmero já existe!\033[m')
    else:
        lista.append(x)
        print('\033[32mValor adicionado com sucesso.\033[m')
    r = input('Quer continuar?\033[34m[S/N]\033[m ').strip().upper() [0]
    if r == 'N':
        break
    while r not in 'NS':
        print('\033[01;31mValor inválido! Presta atenção!\033[m')
        r = input('Quer continuar?\033[34m[S/N]\033[m  ').strip().upper() [0]
print('\033[36m***'*20, '\033[m')
print(f'Você digitou {sorted(lista)}')
print('\033[36m***'*20, '\033[m')
