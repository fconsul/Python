#ler nome e apresentar primeiro e ultimo nome separadamente
nome=str(input('Digite seu nome '))
dividido=nome.split()
print('Primeiro nome é {} e último é {}'.format(dividido[0], dividido[len(dividido)-1]))