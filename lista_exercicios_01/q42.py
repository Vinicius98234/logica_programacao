A_valores = [1, 10, 5]
B_valores = [2, 3, 1]
C_valores = [True, False, True]
D_valores = [False, True, True]
for i in range(len(A_valores)):
    A = A_valores[i]
    B = B_valores[i]
    C = C_valores[i]
    D = D_valores[i]
    resultado = A > B and C or not D
    print(f"Para A={A}, B={B}, C={C}, D={D}, o resultado é: {resultado}")
