from datetime import date
n = int(input('Em que ano nasceu o atleta? '))
atual = date.today().year
idade = atual - n
if idade <= 9:
    print('O atleta possui {} anos e é \033[7mMirim\033[m!'.format(idade))
elif idade <= 14:
    print('O atleta possui {} anos e é \033[7mInfantil\033[m!'.format(idade))
elif idade <= 19:
    print('O atleta possui {} anos e é \033[7mJunior\033[m!'.format(idade))
elif idade <=25:
    print('O atleta possui {} anos e é \033[7mSênior\033[m!'.format(idade))
else:
    print('O atleta possui {} anos e é \033[7mMaster\033[m!'.format(idade))
