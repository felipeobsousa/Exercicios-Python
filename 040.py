# progama que leia duas notas 
# calculcar media 
# mostrar mensagem conforme o sultado
    # aprovado, desaprovado, recuperaçao

n1 = float(input("digite a sua nota: "))
n2 = float(input("digite a sua nota: "))

media = (n1+n2) / 2
print("sua média é: {}".format(media))

if media < 5:
    print("reprovado")
elif media >= 5 and media < 7:
    print("recuperação")
else:
    print("aprovado")