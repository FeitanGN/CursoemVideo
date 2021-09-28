n = int(input('Digite um número: '))
g = n % 2
if g == 0:
    print('{} é um número par.'.format(int(n)))
else:
    print('{} é um número ímpar.'.format(int(n)))
