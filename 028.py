from random import randint
import time

num = randint(0,5)
r = int(input('Tente adivinhar qual numero eu esstou pensando, vc consegue acertar ? I DARE U MOTHERFUCKER'))
print('loadind...')
time.sleep(3)
if r == num:
    print('Parabens seu Nerd, agora vc pode voltar pra sua vida chata')
else:
    print('vai jogar Minecraft que la vc é menos ruim')
