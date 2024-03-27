somaidade=0
contf20=0
maioridadehomem=0
nomevelho=''
for c in range(1,5):
    print('-'*5, '{}ª PESSOA'.format(c), 5*'-')
    nome = input('NOME: '.format(c))
    sexo = input('SEXO: '.format(c)).upper()
    idade=int(input('IDADE: '.format(c)))
    somaidade=somaidade+idade
    if sexo == 'M':
        if c == 1:
            maioridadehomem= idade
            nomevelho=nome
        if idade > maioridadehomem:
                maioredadehomem = idade
    elif sexo == 'F':
        if idade <20:
            if c == 1:
                contf20=1
            else:
                contf20=contf20+1
print('A média de Idade do grupo é de {} anos.'.format(somaidade/4))
print('O nome do homem de maior idade é {}, e ele tem {} anos.'.format(nomevelho,maioridadehomem))
print('No grupo existem {} mulheres menores de 20 anos.'.format(contf20))











