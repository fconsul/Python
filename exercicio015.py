km=float(input('Informe quantos km você rodou com o veículo '))
dias=int(input('Informe por quantos dias foi o aluguel '))
precodias=dias*60
precokm=km*0.15
soma=precodias+precokm
print('Valor a pagar: R$ {}'.format(soma))