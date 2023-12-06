# EXERCÍCIO 2

from abc import ABC, abstractmethod

class CustomDate:

    def __init__(self, day=1, month=1, year=2000):
        if day < 1 or day > 31:
            raise ValueError("Dia inválido")
        if month < 1 or month > 12:
            raise ValueError("Mês inválido")
        if year < 1900 or year > 2100:
            raise ValueError("Ano inválido")
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if day < 1 or day > 31:
            raise ValueError("Dia inválido")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if month < 1 or month > 12:
            raise ValueError("Mês inválido")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000 or year > 2100:
            raise ValueError("Ano inválido")
        self.__year = year

    def __str__(self):
        return "{}/{}/{}".format(self.__day, self.__month, self.__year)

    def __eq__(self, other_date):
        return self.__day == other_date.__day and \
               self.__month == other_date.__month and \
               self.__year == other_date.__year

    def __lt__(self, other_date):
        if self.__year < other_date.__year:
            return True
        elif self.__year == other_date.__year:
            if self.__month < other_date.__month:
                return True
            elif self.__month == other_date.__month:
                if self.__day < other_date.__day:
                    return True
        return False

    def __gt__(self, other_date):
        if self.__year > other_date.__year:
            return True
        elif self.__year == other_date.__year:
            if self.__month > other_date.__month:
                return True
            elif self.__month == other_date.__month:
                if self.__day > other_date.__day:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listaEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []

    @property
    def lista(self):
        return self.__lista  

    def ordenaLista(self):
        '''
        Este método retorna nova lista 
        a partir da ordenação da atual
        '''
        lista = self.__lista
        lista.sort()

        return lista

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        flag = False
        qtde = 0

        while not flag:
            # Solicitar a quantidade de elementos
            qtde = int(input("Quantos elementos vão existir na lista? "))

            if qtde > 0:
                flag = True
            else:
                print("Aviso: Entre com um número a partir de 1.")

        # Solicitar cada elemento
        for i in range(qtde):
            elemento = input(f'Nome {i + 1}: ').capitalize()

            self.__lista.append(elemento)

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        lista_sorteada = self.ordenaLista()
        tamanho = len(lista_sorteada)
        mediana = ""
        indice_mediana = ""
        
        if (tamanho % 2 == 0):
            indice_mediana = tamanho // 2 - 1
        else:
            indice_mediana = tamanho // 2

        # Atribuição da mediana 
        mediana = lista_sorteada[indice_mediana]

        print('A mediana da lista de nomes é', mediana)    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista)

        print('O primeiro nome alfabeticamente é:', menor)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        maior = max(self.__lista)

        print('O último nome alfabeticamente é:', maior)

    def listaEmOrdem(self):
        '''
        Este método percorre e mostra os elementos da lista
        '''
        lista_ordenada = sorted(self.__lista)
        print('LISTA DE NOMES')

        for (index, item) in enumerate(lista_ordenada):
            print(f'Nome {index + 1}: {item}')

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(CustomDate))
        self.__list = []

    @property
    def lista(self):
        return self.__list

    def entradaDeDados(self):
        num_elements = int(input("Quantos elementos na lista de datas? "))
        for _ in range(num_elements):
            day = int(input("Dia: "))
            month = int(input("Mês: "))
            year = int(input("Ano: "))
            new_date = CustomDate(day, month, year)
            self.__list.append(new_date)

    def mostraMediana(self):
        try:
            sorted_list = sorted(self.__list, key=lambda data: (data.year, data.month, data.day))
            size = len(sorted_list)
            if size % 2 == 0:
                middle1 = sorted_list[size // 2 - 1]
                middle2 = sorted_list[size // 2]
                median = f"{middle1} e {middle2}"
            else:
                median = sorted_list[size // 2]
            print("Mediana:", median)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def mostraMenor(self):
        try:
            minimum_date = min(self.__list, key=lambda data: (data.year, data.month, data.day))
            print("Menor data:", minimum_date)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def mostraMaior(self):
        try:
            maximum_date = max(self.__list, key=lambda data: (data.year, data.month, data.day))
            print("Maior data:", maximum_date)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def listaEmOrdem(self):
        '''
        Este método percorre e mostra os elementos da lista
        '''
        lista_ordenada = sorted(self.__lista)
        print('LISTA DE DATAS')

        for (index, item) in enumerate(lista_ordenada):
            print(f'Data {index + 1}: {item}')

    def __str__(self):
        return str(self.__list)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []    

    @property
    def lista(self):
        return self.__lista    

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        qtd_salarios = int(input("Digite o quantidade de salarios: "))
        for item in range(qtd_salarios):
            salario = float(input("Digite salario: "))
            self.__lista.append(salario)
            #self.__lista=sorted(self.__lista)
        return self.__lista
    #fimdef

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        self.__lista=sorted(self.__lista)
        compr = len(self.__lista)
        if compr % 2 == 1:
            print('A mediana dos salários é', self.__lista[compr // 2]) #arredonda pra baixo
        else:
            print('A mediana dos salários é', (self.__lista[compr // 2] + self.__lista[compr // 2 - 1]) / 2)
        #fimse
    #fimdef 

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        print('O menor salário é', self.__lista[0]) 

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        print('O maior salário é', self.__lista[-1]) 
    
    def __str__(self):
        '''
        This method returns a string representation of the object.
        '''
        #return f"DataFruta: lista salario={', '.join(self.__lista)}"
        return ', '.join(self.__lista)

    #fimdef
    def listaEmOrdem(self):
        self.__lista=sorted(self.__lista)
        return str(self)
    #fimdef

class ListaIdades(AnaliseDados):

    def __init__(self):
        super().__init__(type(int))
        self.__lista = []    

    @property
    def lista(self):
        return self.__lista     
    
    def entradaDeDados(self):
        ida = int(input("Quantas idades na lista? "))
        for _ in range(ida):
            idade = int(input("Idade: "))
            self.__lista.append(idade)
            
    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        size = len(sorted_list)
        if size % 2 == 0:
            median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
        else: 
            median = sorted_list[size // 2]
        print("Mediana ", median)
    
    def mostraMenor(self):
        menor_idade = min(self.__lista)
        print("Menor idade: ", menor_idade)
    
    def mostraMaior(self):
        maior_idade = max(self.__lista)
        print("Maior idade: ", maior_idade)

    def listaEmOrdem(self):
        '''
        Este método percorre e mostra os elementos da lista
        '''
        lista_ordenada = sorted(self.__lista)
        print('LISTA DE IDADES')

        for (index, item) in enumerate(lista_ordenada):
            print(f'Idade {index + 1}: {item}')

    def __str__(self):
        return str(self.__lista)
    
def listaNomesSalarios(nomes: ListaNomes, salarios: ListaSalarios):
    for nome, salario in zip(nomes, salarios):
        print(f'{nome} recebe R$ {salario:.2f}')

def reajustaSalario(lista_salarios):
    custo_folha = sum(map(lambda salario: salario * 1.1, lista_salarios))
    print("Custo da folha: " + str(custo_folha))

    for (index, item) in enumerate(lista_salarios):
        lista_salarios[index] = item * 1.1

def modificaData(datas):
    datas_anteriores = filter(lambda data: data.year < 2019, datas)

    for data in datas_anteriores:
        data.day = 1
        print('Data:', str(data))

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()