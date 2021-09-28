
exp = []
x = (input('Digite uma expressão: '))
exp.append(x)
lista = []
for c in range(0, len(x)):
    if '(' in x[c]:
        lista.append('(')
    if ')' in x[c]:
        lista.append(')')
if len(lista) % 2 == 0:
    print('\033[32mO valor é válido.\033[m')
else:
    print('\033[31mO valor não é válido.\033[m')
