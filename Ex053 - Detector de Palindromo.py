frase=input('Digite uma frase ou palavra: ').strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
print('O que você digitou sem espaços foi: {}'.format(junto))
print('O que você digitou, de trás pra frente, sem espaços foi: {}'.format(inverso))
if junto == inverso:
    print('Como podemos ver acima, "{}" é um PALÍNDROMO!'.format(frase))
else:
    print('Como podemos ver acima, "{}" NÃO É um palíndromo.'.format(frase))
