#fatorial while
n = int(input('Digite o número para saber seu fatorial: '))
c = n
x = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    x *= (c)
    c -= 1
print(x)
print('\nO fatorial de \033[32m{}\033[m é \033[31m{}\033[m.'.format(n, x))
print('-=--'*15)
#fatorial for
n = int(input('Digite o número: '))
x = n
print('Calculando {}! = {} x '.format(n, n), end='')
for c in range(n-1, 0, -1):
    print(c, end='')
    print(' x '.format(c) if c > 1 else ' = {}'.format(n), end='')
    n *= c
print('\nO fatorial de \033[32m{}\033[m é \033[31m{}\033[m.'.format(x, n))
print('Fim do programa!')
print('-=--'*15)