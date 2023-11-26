#leia um ano e mostre se é bissexto
ano=int(input('Digite um ano aleatório '))
resto = ano % 4
if resto==0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é ano bissexto'.format(ano))