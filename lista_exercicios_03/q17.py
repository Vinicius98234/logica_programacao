agenda = {}
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def buscar_contato():
    nome = input("Digite o nome do contato: ")
    contato = agenda.get(nome)
    if contato is not None:
        print(f"O número de telefone de {nome} é: {contato}")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def main():
    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            buscar_contato()
        elif escolha == '3':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

main()