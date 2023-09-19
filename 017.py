'''co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'. format(hi)) '''

from math import ceil, hypot

co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = ceil(hypot(ca, co))
print('a hipotenusa vai medir`{}'.format(hi))
