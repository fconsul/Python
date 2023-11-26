#ler um numero inteiro qualquer e mostra na tela se é par ou ímpar
numero = int(input('Digite um número qualquer '))
resto = numero % 2
if resto==0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
