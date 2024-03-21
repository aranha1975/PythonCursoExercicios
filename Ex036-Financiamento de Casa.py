casa=float(input('Digite o Valor da Casa em R$: '))
salario=float(input('Digite o salário mensal do comprador em R$: '))
anos=float(input('Digite a quantidade de anos para o pagamento: '))
parcela=casa/(anos*12)
if parcela <= (0.3*salario):
    print('PARABÉNS, seu financiamento foi aprovado! Você pagará {} parcelas de R${:.2f}.'.format((int(12*anos)), parcela))
else:
    print('Infelizmente, o valor do seu salário não permite o parcelamento de R${:.2f} em {} anos. EMPRÉSTIMO NEGADO'. format(casa,anos))