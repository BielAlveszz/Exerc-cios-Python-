print('Escolha seu Pedido')
print('Cardápio')
print(str('Codigo-Produto-Preço'))
print(str('100-Hot Dog-R$ 1,20'))
print(str('101-Bauru-R$ 1,30'))
print(str('102-Bauru especial-R$ 1,50'))
print(str('103-Hamburguer-R$ 1,20'))
print(str('104-Cheeseburguer-R$ 1,70'))
print(str('105-Suco-R$ 1,50'))
print(str('106-Agua-R$ 1,00'))

cardapio = {
    100: {'produto': 'Hot Dog', 'preco': 1.20},
    101: {'produto': 'Bauru ', 'preco': 1.30},
    102: {'produto': 'Bauru Especial', 'preco': 1.50},
    103: {'produto': 'Hamburguer', 'preco': 1.20},
    104: {'produto': 'Cheeseburguer', 'preco': 1.70},
    105: {'produto': 'Suco', 'preco': 2.20},
    106: {'produto': 'Agua', 'preco': 1.00},
}

codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo_produto in cardapio:
    produto = cardapio[codigo_produto]['produto']
    preco_unitario = cardapio[codigo_produto]['preco']

    valor_total = quantidade * preco_unitario

    print(f"O total a ser pago por {quantidade} {produto}(s) é R${valor_total:.2f}.")
else:
    print("Código do produto inválido.")
