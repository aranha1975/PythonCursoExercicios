maior=0
menor=0
for c in range(1,6):
    peso=float(input('Digite o peso da {}ª pessoa: '.format (c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR PESO digitado foi {} Kg.'.format(maior))
print('O MENOR PESO digitado foi {} Kg.'.format(menor))





