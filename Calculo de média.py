print ('CALCULO DE MÉDIA')

print ('Nota1: ')
Nota1 = int (input ())

print ('Nota2: ')
Nota2 = int (input ())

if (Nota1>10 or Nota2>10):
    print ('NÚMERO INVÁLIDO')
else:
    soma = int(Nota1) + int(Nota2)
    media = soma /2
    if (media>5):
        print ('APROVADO')
    else:
        print('REPROVADO')
        
