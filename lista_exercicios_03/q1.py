def imprimir_numeros_1_a_100():
    print("Números de 1 a 100:")
    print(*range(1, 101))

def imprimir_pares_50_a_100():
    print("Números pares de 50 a 100:")
    print(*range(50, 101, 2))

def contagem_regressiva():
    print("Contagem regressiva:")
    print(*range(10, -1, -1), "Fogo!")

def numeros_pares_ou_impares(ate_valor, escolha):
    tipo_numero = "pares" if escolha.lower() == "pares" else "ímpares"
    print(f"Números {tipo_numero} de 1 até {ate_valor}:")
    
    numeros = [i for i in range(1, ate_valor + 1) if i % 2 == (0 if escolha.lower() == "pares" else 1)]

    print(*numeros)

imprimir_numeros_1_a_100()
imprimir_pares_50_a_100()
contagem_regressiva()

limite_superior = int(input("Digite um valor limite: "))
escolha_usuario = input("Digite 'pares' para números pares ou 'ímpares' para números ímpares: ")

numeros_pares_ou_impares(limite_superior, escolha_usuario)
