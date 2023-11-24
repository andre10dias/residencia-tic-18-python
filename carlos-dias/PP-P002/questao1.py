tarefas = []

def listar_tarefas():
    if not tarefas:
        print("\nNão existem tarefas para serem exibidas.")
    else:
        print("\nLista de Tarefas:\n")
        for idx, tarefa in enumerate(tarefas, start=1):
            status = "[ x ]" if tarefa['concluida'] else "[   ]"
            print(f"{idx} {tarefa['descricao']} {status}")

def adicionar_tarefa():
    nova_tarefa = input("\nInforme a descrição da nova tarefa: ").capitalize()
    tarefas.append({'descricao': nova_tarefa, 'concluida': False})
    print("\nTarefa registrada com sucesso.")

def concluir_tarefa():
    listar_tarefas()
    id_tarefa = int(input("\nInforme o identificador da tarefa que deseja concluir: ")) - 1

    if 0 <= id_tarefa < len(tarefas):
        if not tarefas[id_tarefa]['concluida']:
            tarefas.insert(0, tarefas.pop(id_tarefa))
            tarefas[0]['concluida'] = True
            print("\nTarefa concluída com sucesso.")
        else:
            print("\nEsta tarefa já concluída.")
    else:
        print("\nTarefa não localizada.")

def editar_tarefa():
    listar_tarefas()
    id_tarefa = int(input("\nInforme o identificador da tarefa que deseja editar: ")) - 1

    if 0 <= id_tarefa < len(tarefas):
        nova_descricao = input("\nInforme uma nova descrição para a tarefa: ").capitalize()
        tarefas[id_tarefa]['descricao'] = nova_descricao
        print("\nTarefa editada com sucesso.")
    else:
        print("\nTarefa não localizada.")

# Menu principal
while True:
    print("\n------------ TO DO LIST ------------\n")
    print("[ 1 ] Listar tarefas registradas")
    print("[ 2 ] Registrar uma nova tarefa")
    print("[ 3 ] Marcar uma tarefa como realizada")
    print("[ 4 ] Editar uma tarefa")
    print("[ 0 ] Sair")

    opcao = input("\nSelecione uma opção: ")

    match opcao:
        case '1':
            listar_tarefas()
        case '2':
            adicionar_tarefa()
        case '3':
            concluir_tarefa()
        case '4':
            editar_tarefa()
        case '0':
            print("\nFinalizando programa...")
            break
        case _:
            print("\nOpção inválida.")