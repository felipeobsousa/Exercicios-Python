from math import ceil, sin, radians, cos, tan
angulo = float(input('digite o angulo que vc deseja:'))
seno = sin(radians(angulo))
print('o seno de {} é {:.2f}.'.format(angulo, seno))
cos = cos(radians(angulo))
print('o coseno de {} é {}.'.format(angulo, cos))
tan = tan(radians(angulo))
print('a tangente de {} é {}.'.format(angulo, tan))
