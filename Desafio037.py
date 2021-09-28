n = int(input('Escolha um número para converter: '))
valor = int(input('Digite 1 para binário, 2 para octadecimal ou 3 para hexadecimal: '))
if valor == 1:
    print('O valor em binário é \033[1;31m{}\033[m!'.format(bin(int(n))[2:]))
elif valor == 2:
    print('O valor em octadecimal é \033[1;31m{}\033[m!'.format(oct(int(n))[2:]))
else:
    print('O valor em hexadecimal é \033[1;31m{}\033[m'.format(hex(int(n))[2:]))
