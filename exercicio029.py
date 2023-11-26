#ler velocidade de carro, se for maior que 80 multa de 7 reais por km acima do limite
velocidade=float(input('Digite a velocidade em km/h que seu carro passou pela Marginal Pinheiros '))
acima=(velocidade-80)
if acima>0:
    print('Se ferrou! Tomou multa no valor de R$ {:.2f}'.format(acima * 7))
else:
    print('Velocidade dentro do permitido')