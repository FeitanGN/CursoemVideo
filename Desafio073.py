tabela = ('Atlético.MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 
        'Corintians', 'Cuiabá', 'Fluminense', 'Atlético.GO', 'Athletico.PR', 
        'Ceará', 'Internacional', 'Juventude', 'Santos', 'São Paulo', 'Bahia', 
        'América.MG', 'Sport', 'Grêmio', 'Chapecoense')
pos = tabela.index('Chapecoense')
print('\033[32m-=-'*20)
print(f'\033[36mOs 5 primeiros colocados são:\033[m{tabela[0:5]}')
print('\033[32m-=-'*20, '\033[m')
print(f'\033[36mOs 4 últimos colocado são:\033[m{tabela[-4:]}')
print('\033[32m-=-'*20, '\033[m')
print(f'\033[36mA tabela em ordem alfabética fica:\033[m {sorted(tabela)}')
print('\033[32m-=-'*20)
print('\033[36mA Chapecoense está na posição {} da tabela\033[m.'.format(pos + 1))
print('\033[32m-=-'*20)

