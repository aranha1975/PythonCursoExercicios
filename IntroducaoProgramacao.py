def trabalho(horas):

    if horas > 40:
        horanormal = 40 * 33.3
        horaadicional = ((horas - 40) * 33.3) * 1.25
        print(f'O valor a ser pago é {horanormal+horaadicional}')
    else:
        horanormal = horas * 33.3
        horaadicional = ((horas - 40) * 33.3) * 1.25
        print(f'O valor a ser pago é {horanormal}')
trabalho(int(input('Digite a quantidade de horas trabalhadas: ')))
