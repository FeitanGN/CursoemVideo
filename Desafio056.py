somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor = 0
for p in range(1, 5):
    print('------{}º PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor += 1
media = somaidade / 4
print('A média da idade é {}.'.format(media))
print('O homem mais velho possui {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('{} mulheres ainda não possuem 20 anos.'.format(mulhermenor))
