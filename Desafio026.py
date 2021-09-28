frase = input('Digite uma frase: ').strip().lower()
#frase = 'Alguém disse que nada que o mundo queira é útil!'
print('Vezes que "a" aparece na frase: ', frase.count('a'))
print('Posição que "a" aparece a primeira vez: ', frase.find('a')+1)
print('Posição que "a" aparece na última vês: ', frase.rfind('a')+1)