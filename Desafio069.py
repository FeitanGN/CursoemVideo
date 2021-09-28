#Idade e sexo de várias pessoas
print('\033[31m+-'*20, '\033[m')
print('\033[2;34mCADASTRE UMA PESSOA.\033[m'.center(50))
print('\033[31m+-'*20, '\033[m')
sexo = idade = maior = homens = mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo \033[31m[M/F]\033[m: ')).strip().upper() [0]
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo \033[31m[M/F]\033[m: ')).strip().upper() [0]
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    print('\033[31m--'*20, '\033[m')
    resposta = str(input('\033[31mQuer continuar?\033[36m[S/N]\033[m ')).strip().upper() [0]
    print('\033[31m--'*20, '\033[m')
    if resposta in 'Nn':
        break
    while resposta not in 'SsNn':
        resposta = str(input('\033[31mQuer continuar?\033[36m[S/N]\033[m ')).strip().upper() [0]
print('\033[32m+-'*20, '\033[m')
print(f'{maior} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres têm menos de 20 anos')
print('Encerramos')
print('\033[32m+-'*20, '\033[m')