dias=int(input('Qual a quantidade de dias que você ficou com o carro?'))
km=float(input('Quantos km o você rodou com o carro?'))
preco_dia=60.00
preco_km=0.15
total=(preco_dia*dias)+(preco_km*km)
print('O total a pagar é de R${:.2f}'.format(total))

