n1 = input('Escolha o primeiro número: ')
n2 = input('Escolha o segundo número: ')
n3 = input('Escolha o terceiro número: ')
if n1>n2 and n1>n3:
        print('O maior número é {}'.format(n1))
if n2>n1 and n2>n3:
        print('O maior número é {}'.format(n2))
if n3>n1 and n3>n2:
        print('O maior número é {}'.format(n3))
if n1<n2 and n1<n3:
        print('O menor número é {}'.format(n1))
if n2<n1 and n2<n3:
        print('O menor número é {}'.format(n2))
if n3<n1 and n3<n2:
        print('O menor número é {}'.format(n3))
print('Fim do programa!')
#É possível testar usando um como maior ou menor
#ex: menor = n1
#if n2<n1 and n2<n3:
#menor = n2