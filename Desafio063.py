print('___'*20)
print('Sequência de Fibonacci')
print('___'*20)
n = int(input('Digite o número de termos: '))
t1 = 0
t2 = 1
r = 0
print('0', end=', ')
while r < n - 1:
    r += 1
    g = t1 + t2
    t1 = t2
    t2 = g
    x = t1
    print(x, end=', ')
print('Fim')
print('___'*20)