largura = float(input('largura da parede ? '))
altura = float(input('altura da parede ?'))
area = largura * altura
print('sua parede tem {}x{} e sua area e de {}m²'.format(largura, altura,area ))
tinta = area / 2
print('para pintar a parede vc precisa de {}l de tinta'.format(tinta))