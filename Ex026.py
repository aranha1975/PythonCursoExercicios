frase=str(input('Digite uma frase qualquer: ')).strip().upper()
nome=str(frase.replace('Á','A'))
letra=str(input("Qual letra você quer procurar nessa frase? ")).strip().upper()
print('A letra {} foi encontrada {} vezes na frase'.format(letra.upper(), nome.count(letra.upper())))
print('A primeira vez que a letra {} aparece na frase é na posição {}'.format(letra.upper(), nome.find(letra.upper())+1))
print('A última vez que a letra {} aparece na frase é na posição {}'.format(letra.upper(), nome.rfind(letra.upper())+1))

