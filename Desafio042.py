#Novo desafio dos triângulos
c1 = int(input('Digite primeiro lado: '))
c2 = int(input('Digite segundo lado: '))
c3 = int(input('Digite terceiro lado: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('É possível formar um triângulo', end=' ')
    if c1 == c2 == c3:
        print('Equilátero!')
    elif c1 != c2 != c3 != c1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Não é possível formar um triângulo!')