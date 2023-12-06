
from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia # Atributos "privados" 
        self.__mes = mes # Atributos "privados"
        self.__ano = ano # Atributos "privados"

    @property
    def dia(self): # Get dia
        return self.__dia
    
    @dia.setter
    def dia(self, dia): # Set dia
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self): # Get mes
        return self.__mes
    
    @mes.setter
    def mes(self, mes): # Set mes
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self): # Get ano
        return self.__ano
    
    @ano.setter
    def ano(self, ano): # Set ano
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self): #Generica
        pass

    @abstractmethod
    def mostraMediana(self): #Generica
        pass
    
    @abstractmethod
    def mostraMenor(self): #Generica
        pass

    @abstractmethod
    def mostraMaior(self): #Generica
        pass

    @abstractmethod
    def listarEmOrdem(self): #Generica
        pass
class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []     # Inicializa a lista vazia atributo privado   

    def get(self):
        return self.__lista
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        quantidade = int(input("Quantos de nomes que deseja adicionar? "))

        for i in range(quantidade):
            while True:
                try:
                    elemento = input(f"Digite o {i+1}º nome: ")
                    if not elemento:
                        raise ValueError("Você precisa digitar um nome.") # Tratamento de erro caso o usuário digite um nome vazio
                    
                    self.__lista.append(elemento)
                    break
                except ValueError as e:
                    print(f"Erro: {e} Tente novamente.") # Tratamento de erro

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
         # Ordena a lista
        lista_ordenada = sorted(self.__lista) #self.__lista da minha classe 
        tamanho = len(lista_ordenada) #catura o tamanho da lista
        
        if tamanho == 0: 
            print("A lista está vazia. Não há mediana.")
        elif tamanho % 2 != 0:  # Se a lista tem tamanho ímpar
            # Calcula a mediana para lista ímpar
            mediana = lista_ordenada[tamanho // 2]
            print(f"A mediana é: {mediana}")
        else:  # Se a lista tem tamanho par
            # Calcula a mediana para lista par
            indice_meio = tamanho // 2
            # A lista já esta ordenada portanto o nome está em ordem alfabética
            # Fazendo a divisão do tamanho por 2 obtemos o indice da metade, neste caso a metade é tamanho/2 = x e tamanho/2 = x + 1,
            # entre os dois valores temos que a lista está ordenada portanto o nome está em ordem alfabética tamanho/2 = x, na regra será a mediana;
            primeiro_nome_da_mediana = lista_ordenada[indice_meio -1]
            print(f"O nome da mediana é: {primeiro_nome_da_mediana}")
        

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print("A lista de nomes está vazia.")
            return None
        
        menor_nome = min(self.__lista)  # Encontra o menor nome na lista usando a função min
        #print(f"O menor nome é: {menor_nome}")
        return menor_nome

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print("A lista de nomes está vazia.")
        
        maior_nome = max(self.__lista)  # Encontra o maior nome na lista usando a função max
        #print(f"O maior nome é: {maior_nome}")
        return maior_nome

    def __str__(self):
        '''
        Este método retorna uma representação da lista de nomes
        '''
        #print(f"Lista de nomes: {self.__lista}")

        lista_formatada = ', '.join(str(nome) for nome in self.__lista)
        return f"Lista de nomes: {lista_formatada}"
    
    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        print(f"Lista de Nomes: [{lista_ordenada}]")
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        elementos = int(input("Quantos elementos deseja adicionar? "))
        
        for i in range(elementos):
            try:
                print(f" {i+1}º Data:")
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                nova_data = Data(dia, mes, ano)
                self.__lista.append(nova_data)
            except ValueError as e:
                print(f"Erro: {e}. Data não adicionada.")
        
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
    
        lista_ordenada = sorted(self.__lista)
        meio = len(lista_ordenada) // 2
        
        if len(lista_ordenada) % 2 == 0:
            mediana = lista_ordenada[meio - 1] # Data anterior entre os dois valores do meio lista está ordenada por isso é possivel
        else:
            mediana = lista_ordenada[meio]  # Elemento do meio quando o tamanho da lista é ímpar
        
        print(f"A Data da mediana é: {mediana}")
  
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
    
        menor_data = min(self.__lista)
        #print(f"A menor data é: {menor_data}")
        return menor_data
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None

        maior_elemento = max(self.__lista)
        #print(f"A maior data é: {maior_elemento}")
        return maior_elemento
    
    def __str__(self):
        '''
        Este método retorna uma representação da lista de datas
        '''
        datas_formatadas = ', '.join(str(data) for data in self.__lista)
        #print(f"Lista de Datas: [{datas_formatadas}]")
        return f"Lista de Datas: [{datas_formatadas}]"
    def listarEmOrdem(self):
        datas_ordenadas = sorted(self.__lista)  # Ordena as datas
        datas_formatadas = ', '.join(str(data) for data in datas_ordenadas)
        print(f"Lista de Datas: [{datas_formatadas}]") # imprime a lista ordenada

    def modificarDiasAnteriores2019(self):
        '''
        Este método modifica os dias das datas anteriores a 2019 para o dia 1.
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
        
        for i, data in enumerate(self.__lista):
            if data.ano < 2019:
                self.__lista[i] = Data(1, data.mes, data.ano)  
        
class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        
    def get(self):
        return self.__lista
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        elementos = int(input("Quantos elementos deseja adicionar? "))
        
        for i in range(elementos):
            while True:
                try:
                    print(f"{i+1}º Salário:")
                    salario = float(input("Digite o valor do salário: "))
                    self.__lista.append(salario)
                    break
                except ValueError as e:
                    print(f"Erro: {e}. Por favor, digite um número válido.")

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
        
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            mediana = (lista_ordenada[tamanho // 2] + lista_ordenada[tamanho // 2 - 1]) / 2
        else:
            mediana = lista_ordenada[tamanho // 2]
        
        print(f"O salário da mediana é: {mediana}")

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None

        menor_salario = min(self.__lista)
        #print(f"O menor salário é: {menor_salario}")
        return menor_salario;

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
    
        maior_salario = max(self.__lista)
        #print(f"O maior salário é: {maior_salario}")
        return maior_salario
    
    def __str__(self):
        '''
        Este método retorna uma representação da lista de salário
        '''
        
        lista_formatada = ', '.join(str(salario) for salario in self.__lista)
        #print(f"Lista de Salários: {lista_formatada}")
        return lista_formatada
    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        print(f"Lista de Salarios: [{lista_ordenada}]")

    def ajustarSalarios(self):
        if not self.__lista:
                print("A lista está vazia.")
        else: 
            self.__lista = list(map(lambda x: x * 10 / 100, self.__lista))
            print("\nIterador map - Salários Reajustados em 10%:")
            print(self.__listas)
    def calcularFolha(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
            return 0
        folha_pagamento = sum(self.__lista)
        print(f"Lista de Salarios: [{folha_pagamento}]")
        return folha_pagamento
class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        elementos = int(input("Quantos elementos deseja adicionar? "))

        for i in range(elementos):
            while True:
                try:
                    print(f"{i+1}º Idade:")
                    idade = int(input("Digite a idade: "))
                    self.__lista.append(idade)
                    break
                except ValueError as e:
                    print(f"Erro: {e}. Por favor, digite um número válido.")

    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            mediana = (lista_ordenada[tamanho // 2] + lista_ordenada[tamanho // 2 - 1]) / 2
        else:
            mediana = lista_ordenada[tamanho // 2]
        
        print(f"A idade da mediana é: {mediana}")    
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
        
        menor_idade = min(self.__lista)
        #print(f"A menor idade é: {menor_idade}")
        return menor_idade
        
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return None
        
        maior_idade = max(self.__lista)
        
        #print(f"A maior idade é: {maior_idade}")
        return maior_idade
    

    def __str__(self):
        '''
        Este método retorna uma representação da lista de datas
        '''
        lista_formatada = ', '.join(str(idade) for idade in self.__lista)
        #print(f"Lista de idade: {lista_formatada}")
        return lista_formatada

    def listarEmOrdem(self):
        lista_ordenada = sorted(self.__lista)
        print(f"Lista de Salarios: [{lista_ordenada}]")
        
def percorrerNomeSalario(nomes, salarios):
    if not nomes:
        print("Nenhum nome cadastrado")
        return None
    if not salarios:
        print("Nenhum salário cadastrado")
        return None
    print("Iterando Nomes e Salários:")
    for nome, salario in zip(nomes, salarios):
        print(f"{nome}: R${salario}")
def main():
    nomes = ListaNomes() # Criando uma instância da classe ListaNomes
    datas = ListaDatas()   # Criando uma instância da classe ListaDatas
    salarios = ListaSalarios() # Criando uma instância da classe ListaSalarios
    idades = ListaIdades() # Criando uma instância da classe 2ListaIdades

    # listaListas = [nomes, datas, salarios, idades] # Criando uma lista contendo as listas criadas

    # for lista in listaListas: # Para cada lista na listaListas
    #     lista.entradaDeDados() # Chama o método entradaDeDados da lista 
    #     lista.mostraMediana() # Chama o método mostraMediana da lista
    #     lista.mostraMenor() # Chama o método mostraMenor da lista
    #     lista.mostraMaior() # Chama o método mostraMaior da lista
    #     lista.__str__() # Chama o método __str__ da lista
    #     lista.listarEmOrdem() # Chama o método listarEmOrdem da lista
    #     print("___________________")

    while True:
        print("\n=== Menu ===")
        print("1. Incluir nome na lista de nomes")
        print("2. Incluir salário na lista de salários")
        print("3. Incluir data na lista de datas")
        print("4. Incluir idade na lista de idades")
        print("5. Percorrer listas de nomes e salários")
        print("6. Calcular valor da folha com reajuste de 10%")
        print("7. Modificar dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nomes.entradaDeDados()
            
            pass
        elif opcao == "2":
            salarios.entradaDeDados()
            pass
           
        elif opcao == "3":
            datas.entradaDeDados()
            pass
            
        elif opcao == "4":
            idades.entradaDeDados()
            pass
           
        elif opcao == "5":
             percorrerNomeSalario(nomes.get(), salarios.get())
             pass
           
        elif opcao == "6":
            salarios.ajustarSalarios()
            salarios.calcularFolha()
            pass
           
        elif opcao == "7":
           datas.modificarDiasAnteriores2019()
           pass
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

    #Chama fora mesmo como uma função passando os dois parametros
    #Utilizando o iterador zip para percorrer as listas de nomes e salários simultaneamente
    # # Criar função para dentro de lista salario;
    # # Utilizando o iterador map para reajustar os salários em 10% expressão lambda
  

    
    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
