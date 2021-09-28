print('\033[31m+++'*20, '\033[m')
print(str('Loja dos informados'.center(60)))
print('\033[31m+++'*20, '\033[m')
produto = preço = totalcompra = maior = menor = p = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    p += 1
    if p == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if preço >= 1000:
        maior += 1
    totalcompra += preço
    print('\033[31m---'*20)
    resposta = input('Quer continuar? ')
    print('---'*20, '\033[m')
    if resposta in 'Nn':
        break
print('\033[32m+++'*20)
print('Fechando a conta')
print(f'O total da compra foi R$ {totalcompra:.2f}')
print(f'Temos {maior} produtos que custam mais de R$ 1000,00.')
print(f'O produto mais barato foi {barato} por R$ {menor:.2f}.')
print('+++'*20, '\033[m')