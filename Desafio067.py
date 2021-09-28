#Tabuada sem valor negativo
print('---'*20)
while True:
    print('---'*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('---'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} =', '\033[32m',n*c,'\033[m')
print('\033[31m==='*20)
print('Número negaivo. Acabamos.')
print('==='*20)
print('\033[m')
