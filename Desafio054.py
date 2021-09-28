from datetime import date
atual = date.today().year
menor = 0
maior = 0
for ano in range(1, 8):
    nascimento = int(input('Que ano a {}º pessoa nasceu? '.format(ano)))
    idade = atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Das sete pessoas, \033[3;31m{}\033[m ainda são MENORES de idade e \033[3;31m{}\033[m são MAIORES.'.format(menor, maior))
