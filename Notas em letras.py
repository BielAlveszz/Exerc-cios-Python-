N = int (input('Digite a nota: '))

if (N == 0):
    print('E')
elif (N == 1 or N<36):
    print ('D')
elif (N == 36 or N<61):
    print('C')
elif (N == 61 or N<86):
    print ('B')
elif (N == 86 or N<101):
    print ('A')
else:
    (N>100)
    print ('NÚMERO INVÁLIDO')
