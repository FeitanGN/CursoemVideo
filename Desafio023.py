#Modo string

numero = int(input('Digite um número de 0 a 9999: '))
n1 = '{:0>4}' .format(numero)
print('Unidade: ', n1.strip(' ') [3])
print('Dezena: ', n1.strip(' ') [2])
print('Centena: ', n1.strip(' ') [1])
print('Milhar: ', n1.strip(' ') [0])

#Modo matemático

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}'. format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
