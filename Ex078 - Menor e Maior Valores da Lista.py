valores=[]
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posicao {c}: ')))
    posicao = c
'''maior=menor=valores[0]
posicao=0'''

for n in valores:
    if n == 0:
        maior=menor=valores[0]
    if n > maior:
        maior=n
        posmaior=valores[n]
    if n < menor:
        menor=n
        posmenor=valores[n]

print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi: {maior} e ele está na posição: {posicaomaior}')
print(f'O menor número digitado foi: {menor} e ele está na posição: {posicaomenor}')