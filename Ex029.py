v=float(input('Qual a velocidade do carro, em km/h, ao passar pelo radar? '))
l=float(input('Qual o limite de velocidade da via? '))
t=float(input('Qual a taxa paga em R$ pra cada km acima do limite? '))
if v>l:
    m=(v-l)*t
    print('\033[1;31mVocê ultrapassou o limite de  velocidade da via e receberá uma multa de R${:.2f}.'.format(m))
else:
    print('\033[1;34mParabéns, você se manteve no limite de velocidade de {}km/h'.format(l))
