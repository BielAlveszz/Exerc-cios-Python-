calendario = {
    1: {'mes': 'Janeiro'},
    2: {'mes': 'Fevereiro'},
    3: {'mes': 'Março'},
    4: {'mes': 'Abril'},
    5: {'mes': 'Maio'},
    6: {'mes': 'Junho'},
    7: {'mes': 'Julho'},
    8: {'mes': 'Agosto'},
    9: {'mes': 'Setembro'},
    10: {'mes': 'Outubro'},
    11: {'mes': 'Novembro'},
    12: {'mes': 'Dezembro'},
    }
mes_escolhido = int(input("Digite o numero do mês escolhido: "))

if mes_escolhido in calendario:
    mes_selecionado = calendario[mes_escolhido]['mes']

    print(f"O mês escolhido foi {mes_selecionado}.")
else:
    print("Esse mês não existe!.")

