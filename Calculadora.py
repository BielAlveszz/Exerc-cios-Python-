operation = input('''Qual o tipo de operação?
+ para adição
- para subitração
* para multiplicação
/ para divisão
''')

n1 = int(input('Digite o primeiro numero! : '))
n2 = int(input('Digite o sefundo numero! : '))

if operation == '+':
  print('{} + {} = '.format(n1, n2))
  print(n1 + n2)

elif operation == '-':
  print('{} - {} = '.format(n1, n2))
  print(n1 - n2)

elif operation == '*':
  print('{} * {} = '.format(n1, n2))
  print(n1 * n2)

elif operation == '/':
  print('{} / {} = '.format(n1, n2))
  print(n1 / n2)
else:
  print('Digite uma operação valida e tente novamente.')

