valor = int(input("Digite um valor inteiro: "))
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(valor)
for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula
    print(f"{quantidade} nota(s) de R$ {cedula},00")
    