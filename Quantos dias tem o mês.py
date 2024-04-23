def numero_de_dias(ano, mes):
    meses_31_dias = {1, 3, 5, 7, 8, 10, 12}
    meses_30_dias = {4, 6, 9, 11}

    if mes == 2:
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            return 29
        else:
            return 28
    elif mes in meses_31_dias:
        return 31
    elif mes in meses_30_dias:
        return 30
    else:
        return None

def main():
    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês (1 a 12): "))

    numero_dias = numero_de_dias(ano, mes)

    if numero_dias is not None:
        print(f"O mês {mes} do ano {ano} tem {numero_dias} dias.")
    else:
        print("Mês inválido.")

if __name__ == "__main__":
    main()

