#perguntar salário e calcular 10% de aumento se for maior que 1250 e 15% para menor ou igual
salario = float(input('Digite seu salário em reais '))
if salario <=1250:
    print('Seu aumento será de 15%! Seu aumento será de {} e seu novo salário será de R$ {:.2f}'.format(salario*0.15,salario*1.15))
else:
    print('Seu aumento será de 10%! Seu aumento será de {} e seu novo salário será de R$ {:.2f}'.format(salario*0.10,salario*1.10))