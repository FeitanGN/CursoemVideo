#Tabuada
print('***'*40)
numero = int(input('A tabuada de que número que você quer? '))
for multi in range(1, 11):
    print('{} x'.format(numero), multi, '= {}'.format(numero * multi))
