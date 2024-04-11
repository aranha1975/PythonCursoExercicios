valores=[]
for c in range(1,6):
    valores.append(int(input(f'Digite o {c}º valor: ')))
maior=menor=valores[0]

for n in valores:
    if n>maior:
        maior=n
    if n<menor:
        menor=n
print(f'O maior número digitado foi: {maior} e ele está na {valores.index(maior)+1}ª posição ')
print(f'O menor número digitado foi: {menor} e ele está na {valores.index(menor)+1}ª posição ')