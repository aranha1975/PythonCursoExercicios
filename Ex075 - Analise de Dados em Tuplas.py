numeros=(int(input('Digite um número: ')),int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print('O valor 9 aparece {} {}'.format(numeros.count(9),'vez' if numeros.count(9)==1 else 'vezes'))
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end= '')
for p in numeros:
    if p % 2 == 0:
        print(p,end=' ')
