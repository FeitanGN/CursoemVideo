from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10),)

print('Os números sorteados foram: ', end='')
for f in numeros:
    print(f, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O maior valor sorteado foi {min(numeros)}.')