d = float(input('Digite a distância da viagem em km: '))
if d<=200:
    print('Sua passagem vai custar: R${:.2f}'.format(d*0.5))
else:
    print('Sua passagem vai custar: R${:.2f}'.format(d*0.45))
