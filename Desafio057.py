#sexo apenas f ou m
sexo = str(input('Digite um sexo \033[32m[M/F]\033[m: ')).upper().strip() [0]
#while sexo not in 'MmFf'
while sexo != 'M' and sexo != 'F':
    print('Errado. Tente novamente.')
    sexo = str(input('Digite um sexo \033[31m[M/F]\033[m: ')).upper().strip() [0]
print(f'Sexo {sexo} registrado com sucesso')
print('Fim')