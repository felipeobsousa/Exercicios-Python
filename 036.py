casa = float(input('qual o valor da casa ?: R$ '))
salario = float(input('qual o valor do seu salario ?: R$'))
tempo = int(input('Em quantos anos você quer pagar a casa ?: '))
prestacao = casa / (tempo * 12)

if casa / (tempo * 12) <= 30 / 100 * salario:
    print('seu salario é compativel com o valor da parcela!')
else:
    print('seu salario é incopativel com o valor da parcela')
