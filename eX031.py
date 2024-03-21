d=float(input('Qual a distância total da Viagem? '))
if d<=200:
    print('O valor da passagem é R${:.2f}'.format(d*0.50))
else:
    print('O valor da passagem é R${:.2f}'.format(d*0.45))
