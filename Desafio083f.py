exp = str(input('Digite uma expressão: '))
lista = []
for c in exp:
    if c in '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[32mO valor é válido.\033[m')
else:
    print('\033[31mO valor não é válido.\033[m')

