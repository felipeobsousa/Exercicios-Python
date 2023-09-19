preço1 = float(input('qual o preço do produto ? '))
preço2 = preço1 - (preço1 * 5 / 100)
print('o seu produto custa {:.2f}, e com desconto custará {:.2f}.'.format(preço1, preço2))
