#Condição de parada 999 com break
print('+++'*15)
n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número[999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('+++'*15)
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')
print('+++'*15)
