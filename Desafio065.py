from time import sleep
resposta = int(input('Digite um número: '))
cont = 1
tot = media = maior = menor = resposta
end = str(input('Deseja continuar? [S/N]: ')).strip().upper() [0]
while end not in 'NnSs':
    print('Valor inválido. Tente novamente.')
    end = str(input('Deseja continuar? [S/N]: ')).strip().upper() [0]
if end in 'SsNn':
    while end in 'Ss':
        resposta = int(input('Digite um número: '))
        cont += 1
        tot += resposta
        media = tot / cont
        if resposta > maior:
            maior = resposta
        if resposta < menor:
            menor = resposta
        end = str(input('Deseja continuar? [S/N]: ')).strip().upper() [0]
    if end == 'N':
        print('---'*20)
print('Acabamos então.')
print('Encerrando...Aguarde!')
sleep(2)
print('---'*20)
print('Você digitou \033[32m{}\033[m números e a média dos valores é \033[32m{:.2f}\033[m'.format(cont, media))
print('O maior valor lido é \033[32m{}\033[m e o menor é \033[32m{}\033[m'.format(maior, menor))
print('---'*20)
