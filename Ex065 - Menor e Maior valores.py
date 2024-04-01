continuar='s'
cont=soma=0
maior=0
menor=0
while continuar.upper() == 'S':
    n=int(input('Digite um número: '))
    cont+=1
    soma=soma+n
    if cont == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    continuar=input('Quer continuar? [S] ou [N] ? ')
    if continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar = input('Opção inválida.\nQuer continuar? [S] ou [N] ? ')
print('acabou. Você digitou {} números e a média foi de {}'.format(cont,soma/cont))
print('O maior número digitado foi {} e o menor {}.'.format(maior,menor))
