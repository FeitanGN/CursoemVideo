print('\033[31m+++'*20, '\033[m')
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('\033[31m+++'*20, '\033[m')
valor = int(input('Qual valor você deseja sacar? R$'))
print('\033[32m+++'*20, '\033[m')
total = valor
céd = 50
notas = 0
while True:
    if total >= céd:
        total -= céd
        notas += 1
    else:
        if notas > 0:
            print(f'Você receberá {notas} notas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        notas = 0
        if total == 0:
            break
print('\033[32m+++'*20, '\033[m')
print('{:^60}'.format('Obrigado por sacar aqui.'))
print('\033[32m+++'*20, '\033[m')
