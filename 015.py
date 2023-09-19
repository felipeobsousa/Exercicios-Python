km = float(input('quantos KMs rodados? '))
dias = int(input('quantos dias alugados? '))
#km1 = km * 0.15
#dias1 = dias * 60
#print('sua divida é de R${:.2f}'.format(km1 + dias1))
pagar = km * 0.15 + dias * 60
print('sua divida é de {:.2f}'.format(pagar))