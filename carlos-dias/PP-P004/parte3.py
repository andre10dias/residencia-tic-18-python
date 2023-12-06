# EXERCÍCIO 3

from exc1 import *
from exc2 import *

def montarMenu(opcoes):
    opcoes_size = len(opcoes)

    for i in range(opcoes_size + 1):
        if ( i == opcoes_size ):
           print('0. Sair do programa')
        else:
           print(f'{i + 1}. {opcoes[i]}')

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    opcoes = [ 'Incluir um nome na lista de nomes',
                'Incluir um salário na lista de salários',
                'Incluir uma data na lista de datas',
                'Incluir uma idade na lista de idades',
                'Percorrer as listas de nomes e salários',
                'Calcular o valor da folha com um reajuste de 10%',
                'Modificar o dia das datas anteriores a 2019' ]
    opcoes_size = len(opcoes)

    while True:
        montarMenu(opcoes)
        
        opcao_usuario = int(input('\nSua opção: '))
        
        if (not (opcao_usuario > opcoes_size)):
            print('-' * 20)
        
        match opcao_usuario:
            case 0:     # Finalizar programa
                print('Fim do programa!')
                break

            case 1:     # Incluir nome
                nomes.entradaDeDados()
                
            case 2:     # Incluir salário
                salarios.entradaDeDados()

            case 3:     # Incluir data
                datas.entradaDeDados()

            case 4:     # Incluir idade
                idades.entradaDeDados()

            case 5:     # Percorrer nomes e salários
                listaNomesSalarios(nomes.lista, salarios.lista)

            case 6:     # Calcular reajuste
                reajustaSalario(salarios.lista)

            case 7:     # Modificar antes de 2019
                modificaData(datas.lista)

            case _:
                print('Insira um número entre 0 e', opcoes_size)
            
        print() # Simples quebra de linha após execução de módulo


if __name__ == "__main__":
    main()