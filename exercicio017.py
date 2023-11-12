import math
cateto1=float(input('Digite a medida de um dos catetos do triângulo retângulo '))
cateto2=float(input('Digite a medida do outro cateto '))
hipotenusa=math.hypot(cateto1,cateto2)
print('A medida da hipotenusa dos catetos {:.2f} e {:.2f} é {:.2f}'.format(cateto1, cateto2, hipotenusa))