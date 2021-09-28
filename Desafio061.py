termo = int(input('Digite o termo da progressão aritmética: '))
p = int(input('Digite a razão: '))
h = 11
while h > 1:
    termo += p
    h -= 1
    print(termo, end=', ')
print('FIM')