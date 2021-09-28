n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Sua média foi \033[1;33m{}\033[m. Você foi \033[1;32maprovado\033[m. Bora comemorar!'.format(media))
elif media >= 5:
    print('Sua média foi \033[1;33m{}\033[m. Você está em \033[1;33mrecuperação\033[m! Vai estudar.'.format(media))
elif media < 5:
    print('Sua média foi \033[1;33m{}\033[m. Você foi \033[1;31mreprovado\033[m! Volte no ano que vem.'.format(media))
