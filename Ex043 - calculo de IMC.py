peso=float(input('Informe seu Peso em Kg: '))
altura=float(input('Informa sua Altura em metros: '))
imc=peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é {:.1f}'.format (imc))
    print('Voce está BAIXO DO PESO NORMAL')
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Voce está COM PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Voce está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Voce está com OBESIDADE')
else:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Voce está com OBESIDADE MÓRBIDA')
