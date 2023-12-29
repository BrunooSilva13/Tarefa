#!/bin/python3

def mostrar_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair")

# Lista para armazenar as tarefas
tarefas = []

while True:
    mostrar_menu()

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        # Adicionar tarefa
        nova_tarefa = input("Digite o nome da nova tarefa: ")
        tarefas.append({"tarefa": nova_tarefa, "concluida": False})
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

    elif escolha == "2":
        # Visualizar tarefas
        print("\n=== Lista de Tarefas ===")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluida"] else "Não Concluída"
            print(f"{i}. {tarefa['tarefa']} - {status}")

    elif escolha == "3":
        # Marcar tarefa como concluída
        if not tarefas:
            print("Lista de tarefas vazia.")
        else:
            try:
                indice_concluir = int(input("Digite o número da tarefa concluída: "))
                if 1 <= indice_concluir <= len(tarefas):
                    tarefas[indice_concluir - 1]["concluida"] = True
                    print("Tarefa marcada como concluída.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif escolha == "4":
        # Sair do programa
        print("Saindo do Gerenciador de Tarefas. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
