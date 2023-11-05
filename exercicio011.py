l=float(input('Informe a largura da sua parede '))
h=float(input('Informe a altura da sua parede '))
area=l*h
#cada litro pinta 2m2
tinta=area/2
print('A área da sua parede é {} e precisa de {} latas de tinta para pintar'.format(area, tinta))
