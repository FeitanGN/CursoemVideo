print('__'*20)
print('Diferentes de 999')
print('__'*20)
n = 0
q = 0
tot = 0
n = int(input('Digite um número: '))
while n != 999:    
    q += 1
    tot += n
    n = int(input('Digite um número: '))
print(f'Vovê digitou {q} números exceto 999.')
print(f'A soma entre eles é {tot}')
print('Fim do programa.')
