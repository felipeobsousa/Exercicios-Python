# como eu fiz.

'''velocidade = float(input('qual foi a velocidade do carro ?'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    print('voce deve pagar uma multa de R$ {:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')'''

# resoluçao do exercicio

velocidade = float(input('qual foi a velocidade do carro ?'))
if velocidade > 80:
    print('Multado! voce excedeu o limite permitido de 80Km/h')
    multa = (velocidade - 80) * 7
    print('voce deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom Dia! Dirija com segurança!')