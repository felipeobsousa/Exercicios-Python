import time
print('nossas viagens custam R$ 0.50 por Km e R$ 0.45 por Km para viagens acima de 200Km7')
print('aguarde um momento...')
time.sleep(3)
distancia = float(input('qual a distancia da sua viagem ?'))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print('a sua viagem de {} km custará R$ {:.2f}'.format(distancia,preco))

