#fatorial=1
#numero=int(input('Digite um número para calcular o fatorial: '))
#print('Calculando... {}! = '.format(numero), end='')
#while numero > 0:
#    print(numero, end='')
#    if numero > 1:
#        print(' x ', end='')
#    else:
#        print(' = ', end='')
#        print(fatorial, end='')
#    fatorial = fatorial * (numero)
#    numero = numero - 1

fatorial=1
numero=int(input('Digite um número para calcular o fatorial: '))
print('Calculando... {}! = '.format(numero), end='')
for c in range(numero, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
        print(fatorial, end='')
    fatorial = fatorial * (numero)
    numero = numero - 1



