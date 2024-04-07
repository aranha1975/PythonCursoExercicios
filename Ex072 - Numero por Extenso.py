contagem=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
          'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
          'Dezenove', 'Vinte')
continuar='S'
while continuar.upper() in 'SN':
    numero=int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {contagem[numero]}')
    continuar=str(input('Você quer continuar? [S] ou [N] :'))
    if continuar.upper() == 'N':
        break
print('Obrigado por utilizar o nosso programa.')
