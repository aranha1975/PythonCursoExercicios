#DESAFIO 22
#Crie um programa que leia o nome completo de uma pessoa e montre:
#O nome com todas as letras maiúsculas
#O nome com todas as  letras Minusculas
#Quantas letras tem ao todo (sem considerar  espaços)
#Quantas letras tem o primeiro nome

frase=str(input('Digite seu nome completo: ')).strip()
espaços=(frase.count(' '))
caracteres=len(frase)
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.' .format(frase.upper()))
print('Seu nome  em minúsculas é {}.'.format(frase.lower()))
print('Seu nome tem {} letras.'.format(caracteres-espaços))
pe=int(frase.find(' '))
#print('O seu primeiro nome é {} e ele é formado por {} letras.'.format(frase[0:pe],pe))
separado=frase.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(separado[0], len(separado[0])))
print('O seu segundo nome é {} e ele tem {} letras.'.format(separado[1], len(separado[1])))

