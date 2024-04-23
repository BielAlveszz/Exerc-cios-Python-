import math

def calcular_raizes(a, b, c):
    # Verifica se a é diferente de zero
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    
    # Calcula o delta
    delta = b**2 - 4*a*c
    
    # Verifica o valor do delta
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

def main():
    print("Este programa calcula as raízes de uma equação do segundo grau na forma ax^2 + bx + c.")
    a = float(input("Digite o valor de a: "))
    
    # Verifica se a é zero
    if a == 0:
        print("A equação não é do segundo grau. Encerrando o programa.")
        return
    
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    calcular_raizes(a, b, c)

if __name__ == "__main__":
    main()

