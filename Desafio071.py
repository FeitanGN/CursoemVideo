#notas de 50, 20, 10, 1
print('\033[31m+++'*20, '\033[m')
print('CAIXA ELETRÔNICO'.center(60))
print('\033[31m+++'*20, '\033[m')
valor = int(input('Qual valor você deseja sacar? R$'))
print('\033[32m+++'*20, '\033[m')
sobra = nota50 = nota20 = nota10 = nota1 = 0
if valor > 0:
    if valor >= 50:
        nota50 = valor // 50
        valor -= (nota50*50)
        print(f'Você receberá {nota50} notas de 50')
    if valor < 50 and valor > 20:
        nota20 = valor // 20
        valor -= (nota20*20)
        print(f'Você receberá {nota20} notas de 20')
    if valor < 20 and valor >= 10:
        nota10 = valor // 10
        valor -= (nota10*10)
        print(f'Você receberá {nota10} notas de 10')
    if valor < 10 and valor >= 1:
        nota1 = valor // 1
        valor -= nota1
        print(f'Você receberá {nota1} notas de 1')
print('\033[32m+++'*20, '\033[m')
