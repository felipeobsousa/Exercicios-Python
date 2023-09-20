# progam que leia o ano de nascimento e mostre sua categoria 
# categorias
# ate 9 - mirim 
# ate 14 - infantil 
# ate 19 - junior 
# ate 25 - senior 
# acima - master 

import time


nasc = int(input("digite seu ano de nascimento:"))
idade =  2023 - nasc
print("sua idade é: {}".format(idade))
time.sleep(1)

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Senior")
else:
    print("Master")