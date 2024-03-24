from datetime import date
ano=int(input('Qual o ano de nascimento do atleta? '))
idade=(date.today().year)-ano
if idade <= 9:
    categoria='MIRIM'
elif idade > 9 and idade <= 14:
    categoria='INFANTIL'
elif idade > 14 and idade <= 19:
    categoria='JÚNIOR'
elif idade > 19 and idade <= 25:
    categoria='SÊNIOR'
else:
    categoria='MASTER'

print ('O Atleta tem {} anos.'.format(idade))
print('Ele pertence à categoria {}'. format(categoria))

