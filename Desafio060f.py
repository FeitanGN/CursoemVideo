from math import factorial
n = int(input('Digite um número para calclar seu fatorial: '))
f = factorial(n)
print('O fatorial de \033[32m{}\033[m é \033[31m{}\033[m'.format(n, f))