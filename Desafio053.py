#palíndromo
frase = str(input('Digite uma frase: ')).upper().strip()
#frase = str('Ana').strip().upper()
#separa a frase em palavras separadas
separado = frase.split()
#junta o valor dos espaços com o valor dos asteriscos no meio
junto = ''.join(separado)
#valor para contar para trás
invertido = ''
invertido = junto[::-1]
#laço última letra menos um, até a primeira menos 1 e reduzindo de 1 em 1
'''for letra in range(len(junto) -1, -1, -1):
    #valor será resultado da palavra sem espaços menos a letra reduzindo
    invertido += junto[letra]
print('O inverso de {} é {}.'.format(junto, invertido))'''
if invertido == junto:
    print('É UM PALÍNDROMO.')
else:
    print('NÃO É UM PALÍNDROMO.')