lista_de_tarefas = []

def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)

def exibir_tarefas():
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        print(f"{i}. {tarefa}")

