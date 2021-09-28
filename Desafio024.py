from typing import overload


cidade = input('Digite o nome da sua cidade: ').strip()
#c1 = ('Santo' in cidade)
#print('Existe a palavra Santo na sua cidade? ', c1)
c1 = cidade.strip().upper().split(' ') [0]
v1 = c1 == 'SANTO'
print('Sua cidade inicia com a palavra Santo? ', v1)
