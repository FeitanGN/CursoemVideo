#Número primo
# Regra, ser diferente do número dividido e sobra da divisão ser diferente de zero
#número pra testar
g = int(input('Digite um número: '))
h = 0
for c in range(1, g+1):
    if g % c == 0:
        print('\033[32m', end='')
        h += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if h == 2:
        print('\n\033[mO número {} foi divisível {} vezes, portanto é primo.'.format(g, h))
else:    
    print('\n\033[mO número {} foi divisível {} vezes, portanto não é primo.'.format(g, h))