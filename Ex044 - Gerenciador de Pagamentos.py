print('='*20,'LOJAS ARANHA','='*20)
compras=float(input('Preço das compras: '))
opcao=int(input('FORMAS DE PAGAMENTO:\n[1] À vista dinheiro/cheque\n[2] À vista Cartão de crédito\n[3] 2x no Cartão de crédito\n[4] 3x ou mais no cartão de crédito\nDigite sua opção: '))
if opcao==1:
    print('Sua compra de R${:.2f} será paga À VISTA, com 10% de desconto, totalizando R${:.2f}.'.format(compras,(compras-(compras*0.1))))
elif opcao==2:
    print('Sua compra de R${:.2f} será À VISTA NO CARTÃO, com 5% de desconto, totalizando R${:.2f}'.format(compras,(compras-(compras*0.05))))
elif opcao==3:
    print('Sua compra de R${:.2f} será paga em 2X NO CARTÃO e não terá desconto, nem acréscimo, totalizando {:.2F}'.format(compras,compras))
elif opcao==4:
    parcelas=int(input('Quer pagar em quantas parcelas? '))
    print('Sua compra de R${:.2f} será paga em {:.2f} parcelas de R${:.2f}, totalizando R${:.2f}.'.format(compras, parcelas, ((compras*1.2)/parcelas), (compras*1.2)))
else:
    print('você digitou uma opção inválida. Tente novamente.')


