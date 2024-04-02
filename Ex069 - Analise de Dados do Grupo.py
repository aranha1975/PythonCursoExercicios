cont18=contm=contf20=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade=int(input('Idade: '))
    sexo = ''
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        sexo=input('Sexo [M ou F]: ')
        print('-' * 20)
    if idade > 18:
        cont18=cont18+1
    if sexo.upper() == 'M':
        contm=contm+1
    if sexo.upper() == 'F' and idade < 20:
        contf20=contf20+1
    continuar = ''
    while continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar=input('Quer continuar? [S ou N]: ')
    if continuar.upper() == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Total de Homens cadastrados: {contm}')
print(f'Total de mulheres com menos de 20 anos: {contf20}')