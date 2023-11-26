#verificar se o nome da cidade começa com santo
cidade=input('Digite o nome da sua cidade ').strip()
dividido=cidade.split()
print('santo' in dividido[0].lower())
#print(cidade[:5].upper()=='SANTO')