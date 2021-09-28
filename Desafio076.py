lista = ('Seguro', 30, 'AP', 20, 'Previdência', 100,
 'Capitalização', 50, 'Tarifa', 34, 'Ad Depositante',
  57, 'Cheque Especial', 8, 'Cartão', 17)
print('\033[32m---'*20)
print('LISTAGEM DE PREÇO'.center(60))
print('---'*20, '\033[m')
for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'\033[33m{lista[p]:.<50}', end='')
    else:
        print(f'R$ {lista[p]:>-6.2f}', '\033[m')
print('\033[32m---'*20, '\033[m')
