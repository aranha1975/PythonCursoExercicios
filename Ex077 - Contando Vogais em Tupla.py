palavras=('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
          'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO')
vogais=('A', 'E', 'I', 'O', 'U' )
for i in palavras:
    print(f'\nNa palavra {i} temos: ', end='')
    for c in vogais:
        if c in i:
            print(c, end=' ')

