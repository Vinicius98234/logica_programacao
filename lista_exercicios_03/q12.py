#Contagem Regressiva Recursiva:
def contagem_regressiva_recursiva(n):
    if n == 0:
        print("Fogo!")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

n_recursivo = int(input("Digite um número para a contagem regressiva recursiva: "))
contagem_regressiva_recursiva(n_recursivo)
#Contagem Regressiva Iterativa:
def contagem_regressiva_iterativa(n):
    while n >= 0:
        if n == 0:
            print("Fogo!")
        else:
            print(n)
        n -= 1

n_iterativo = int(input("Digite um número para a contagem regressiva iterativa: "))
contagem_regressiva_iterativa(n_iterativo)

