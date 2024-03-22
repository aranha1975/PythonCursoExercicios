n1=float(input('Digite a 1ª nota: '))
n2=float(input('Digite a 2ª nota: '))
media=(n1+n2)/2
if media<5:
    print('Sua média foi {:.2f}. Você está REPROVADO.'.format(media))
elif media<7 and media>=5:
    print('Sua média foi {:.2f}. Você vai pra PROVA FINAL.'.format(media))
else:
    print('Sua média foi {:.2f}. Voce foi APROVADO, Parabéns!'.format(media))
