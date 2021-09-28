r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))
if r1>r2 and r1>r3:
    h = r1
    c1 = r2
    c2 = r3
elif r2>r1 and r2>r3:
    h = r2
    c1 = r1
    c2 = r3
else:
    h = r3
    c1 = r1
    c2 = r2
if c1-c2<h<c1+c2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!') 
#outro cálculo pode ser 
#r1 < r2+r3 and r2 < r1+r3 and r3<r1+r2