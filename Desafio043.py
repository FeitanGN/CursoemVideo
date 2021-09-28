p = float(input('Digite seu peso em kg: '))
a = float(input('Digite sua altura em m: '))
imc = p / a**2
print('IMC é {:.2f}'.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
