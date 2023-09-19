from datetime import date

nasc = int(input('seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

print('quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))

if idade == 18:
    print('você está na hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    alistamento = ano + saldo
elif idade > 18:
    saldo = idade - 18
    alistamento = ano - saldo
    print('vc já deveria ter se alistado há {} anos.'.format(saldo))
    print('o seu alistamento foi há {} anos'.format(alistamento))