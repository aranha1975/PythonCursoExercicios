listagem=('Arroz', 2.45, 'Feijão', 6.50, 'Sal', 1.89, 'Açúcar', 3.99,
          'Bolacha', 2.30, 'Biscoito Recheado', 2.90, 'Vinagre', 1.80,'Suco', 10.85)
print('-'*37)
print(f'{"LISTA DE PREÇOS":^37}')
print('-'*37)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R$ {:.>.2f}'.format(listagem[pos]))