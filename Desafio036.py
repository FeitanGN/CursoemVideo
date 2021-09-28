print('\033[7mVamos lhe ajudar a verificar sua compra.\033[m')
v = float(input('Digite o valor do imóvel: '))
s = float(input('Digite seu salário: '))
t = int(input('Em quantos anos você deseja pagar? ')) * 12
pmt = v / t
n = s * 0.3
if n>=pmt:
    print('\033[1;32mO valor da parcela é R${:.2f}, e você está apto a financiar. Vamos preparar a papelada!"\033[m'.format(n))
else:
    print('\033[1;31mInfelizmente não será possível efetivar o empréstimo! O valor da parcela é R${:.2f} e passa de 30% da sua renda.\033[m'.format(pmt))
