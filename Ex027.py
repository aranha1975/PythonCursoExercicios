nome=str(input('Qual o seu nome completo? '))
lista=nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é \033[1;34m{}\033[m.'.format(lista[0]))
print('Seu último nome é \033[1;31m{}\033[m.'.format(lista[-1]))

