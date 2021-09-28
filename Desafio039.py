import datetime
n = int(input('Digite o ano em que nasceu: '))
g = datetime.date.today().year
idade = g - n
if idade < 18:
    print('Você ainda vai se alistar no serviço militar, faltam apenas {} anos!'.format(18-idade))
elif idade == 18:
    print('É hora de se alistar, você completou 18 anos!')
else:
    print('Você já passou {} ano(s) do tempo do alistamento!'.format(idade-18))
