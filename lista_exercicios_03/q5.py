while True:
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha uma opção (1 a 5): ")

    if escolha == '5':
        print("Saindo do programa. Até logo!")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida. Escolha novamente.")
        continue

    numero = int(input("Digite um número para a tabuada: "))

    if escolha == '1':
        operacao = "Adição"
        for i in range(1, 11):
            resultado = numero + i
            print(f"{numero} + {i} = {resultado}")
    elif escolha == '2':
        operacao = "Subtração"
        for i in range(1, 11):
            resultado = numero - i
            print(f"{numero} - {i} = {resultado}")
    elif escolha == '3':
        operacao = "Multiplicação"
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} * {i} = {resultado}")
    elif escolha == '4':
        operacao = "Divisão"
        for i in range(1, 11):
            resultado = numero / i
            print(f"{numero} / {i} = {resultado}")
