import os
# Lista de tarefas (usando tuplas para cada tarefa)
tasks = []
# Caminho do arquivo de tarefas
file_path = 'PP-P002/tarefas.txt'
# Carregar tarefas de um arquivo
def carregar_tarefas():
    try:
        with open(file_path, 'r') as file:
            for line in file:
                task_info = line.strip().split(',')  # Separa os dados da tarefa
                tasks.append((int(task_info[0]), task_info[1], task_info[2]))  # Adiciona a tarefa à lista
    except FileNotFoundError:
        pass  # Se o arquivo não existir, não carrega nada

# Salvar tarefas em um arquivo
def salvar_tarefas():
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(f"{task[0]},{task[1]},{task[2]}\n")  # Escreve os dados da tarefa no arquivo

# Adicionar uma nova tarefa
def Add_tarefa(Descrição):
    #ler tamnho da lista e incrementar +1 para o proximo, adicionar a tarefa no final usando append 
    tasks.append((len(tasks) + 1, Descrição, "[ ]"))  # ID, descrição, status inicial
    print("Tarefa registrada!!!")
# Marcar uma tarefa como realizada
def Completar_task(id):
    #len(tasks): Retorna o número de elementos na lista tasks.
    #Verificar o intervalos entre a primeira e ultima tarefa
    if 1 <= id <= len(tasks):
        task = tasks.pop(id - 1)  # Remove a tarefa da posição atual e a armazena
        task = (task[0], task[1], "[x]")  # Atualiza o status para concluída
        tasks.insert(0, task)  # Insere a tarefa no início da lista
        print("Tarefa marcada como realizada!!!")
    else:
        print("Tarefa não encontrada.")
# Editar uma tarefa
def editar_task(id, nova_descrição):
    #Verificar o intervalos entre a primeira e ultima tarefa
    if 1 <= id <= len(tasks):
        #lista começa em 0 e vai ate o final n-1 
        tasks[id - 1] = (tasks[id - 1][0], nova_descrição, tasks[id - 1][2])  # Atualiza a descrição
        print("Tarefa editada com sucesso!!!")

# Exibir a lista de tarefas
def Exibir_tasks():
    if not tasks:
        print("Não há tarefas registradas.")
    else:
        print("Tarefas:")
        for tafefa in tasks:
            print(f"{tafefa[0]}. {tafefa[1]} {tafefa[2]}")  # Mostra ID, descrição e status

carregar_tarefas()
# Menu principal
while True:
    print("\n===== ToDoList =====")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("0. Sair")

    opção = input("Escolha uma opção: ")
    if opção == "1":
        Exibir_tasks()
    elif opção == "2":
        descrição = input("Digite a descrição da tarefa: ")
        Add_tarefa(descrição.capitalize())
        salvar_tarefas()
    elif opção == "3":
        while True:
            try:
                id = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
                Completar_task(id)
                salvar_tarefas()
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                print("Por favor, digite um número inteiro para o ID da tarefa.")
    elif opção == "4":
        while True:
            try:
                id = int(input("Digite o ID da tarefa a ser editada: "))
                descrição = input("Digite a nova descrição da tarefa: ")
                editar_task(id, descrição.capitalize())
                break  # Se a conversão para int for bem-sucedida, sai do loop
                salvar_tarefas()
            except ValueError:
                print("Por favor, digite um número inteiro para o ID da tarefa.")
    elif opção == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
