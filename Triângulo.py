lado1 = int(input('Digite o tamanho do primeiro lado do triângulo: '))
lado2 = int(input('Digite o tamanho do segundo lado do triângulo: '))
lado3 = int(input('Digite o tamanho do terceiro lado do triângulo: '))

if lado1 + lado2 + lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print('Os lados formam um triângulo equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Os lados formam um triângulo isósceles.')
    else:
        print('Os lados formam um triângulo escaleno')
else:
    print('Os lados não formam um triângulo')
  
