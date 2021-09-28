n = input('Digite um nome: ').strip()
nome = n.split()
#nome = ('João Alberto de Albuquerque Batista').strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}!'.format(nome[0]))
print('Seu último nome é {}!'.format(nome[len(nome)-1]))

