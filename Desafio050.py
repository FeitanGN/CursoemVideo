#Soma dos pares
s = 0
for n in range(0, 6):
    m = int(input('Digite um número:' ))
    if m % 2 == 0:
        s += m
print('a Soma dos valores pares é {}.'.format(s))
