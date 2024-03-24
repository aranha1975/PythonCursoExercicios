l1=float(input('Insira a medida do 1º lado: '))
l2=float(input('Insira a medida do 2º lado: '))
l3=float(input('Insira a medida do 3º lado: '))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1==l2==l3:
        print('Os segmentos acima podem forma foram um triângulo EQUILÁTERO.')
    elif l1!=l2!=l3!=l1:
        print('Os segmentos acima podem forma foram um triângulo ESCALENO.')
    else:
        print('Os segmentos acima podem forma foram um triângulo ISÓCELES.')
else:
    print(' Os segmentos informados NÃO PODEM FORMAR UM TRIÊNGULO.')
