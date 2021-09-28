n = ('zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte')
print('\033[32m+++'*20)
print('POR EXTENSO'.center(60))
print('+++'*20, '\033[m')
c = 'S'
while c == 'S':
    if c == 'N':
        break
    while True:
        número = int(input('Digite um número de 0 a 20: '))
        if número > 20 or número < 0:
            print('Valor não está entre 0 e 20, digite novamente.')
        else:
            break        
    print(f'O número {número} se escreve \033[35m{n[número]}\033[m por extenso.')
    c = (input('Quer continuar?[S/N] ')).strip().upper() [0]
    while c not in 'NS':
        c = (input('Quer continuar?[S/N] ')).strip().upper() [0]
print('\033[32m+++'*20)
print('Encerramos'.center(60))
print('+++'*20, '\033[m')