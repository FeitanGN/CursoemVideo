palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'FUTURO', 'GRATIS', 'PRATICAR', 'ESTUDAR', 'CURSO')
print('\033[31m++++'*10)
print('CONTADOR DE VOGAIS'.center(40))
print('++++'*10, '\033[m')
cont = len(palavras)
for r in palavras:
    print(f'\nA palavra \033[32m{r}\033[m possui ', end=' ')
    for v in r:
        if v == 'A':
            print('a', end=' ')
        elif v == 'E':
            print('e', end=' ')
        elif v == 'I':
            print('i', end=' ')
        elif v == 'O':
            print('o', end=' ')
        elif v == 'U':
            print('u', end=' ')
        print(end='')
        cont -= 1
print('\n')
print('\033[31m++++'*10)
print('ENCERRADO'.center(40))
print('++++'*10, '\033[m')