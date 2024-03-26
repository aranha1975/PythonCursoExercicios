from datetime import date
atual= date.today().year
cont=0
for c in range(7):
    ano=int(input('Qual o ano de nascimento da {}ª pessoa: '.format(c+1)))
    idade=atual-ano
    if idade > 21:
        cont+=1
print('{} pessoas são MAIORES DE 21 ANOS'.format(cont))
print('{} pessoas são MENORES DE IDADE'.format(7-cont))