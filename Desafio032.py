import datetime
ano = int((input('Escolha o ano que deseja saber se é bissexto: ')))
if ano == 0:
    ano = datetime.date.today().year #usa date do datetime e apenas o ano do dia atual
if ano%4==0 and ano%100!=0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))
