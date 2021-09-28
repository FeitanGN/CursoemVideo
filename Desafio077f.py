palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON',
            'FUTURO', 'GRATIS', 'PRATICAR',
            'ESTUDAR', 'CURSO')
print('\033[31m++++'*10)
print('\033[01;34mCONTADOR DE VOGAIS'.center(50), '\033[m')
print('\033[31m++++'*10, '\033[m')
cont = len(palavras)
for p in palavras:
    print(f'\n\033[mA palavra \033[32m{p}\033[m possui ', end='\033[32m ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n')
print('\033[31m++++'*10)
print('\033[01;34mENCERRADO'.center(50), '\033[m')
print('\033[31m++++'*10, '\033[m')