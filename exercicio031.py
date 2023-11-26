#perguntar distancia da viagem em km, cobrar 0,50 por km até 200km, 0,45 para maior
distancia = float(input('Digite a distância da sua viagem em km '))
if distancia >=200:
    print('O preço da sua passagem será R$ {:.2f}'.format(distancia*0.5))
else:
    print('O preço da sua passagem será {:.2f}'.format(distancia*0.45))