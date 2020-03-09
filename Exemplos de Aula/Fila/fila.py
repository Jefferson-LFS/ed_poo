class Fila:
    def __init__(self):
        self.__dados = [ ]
        print("Funcao __init__")

    def getFila(self):
        return self.__dados
    
    def inserirDado(self,novoValor):
        self.__dados.append(novoValor)

    def remover(self):
        self.__dados.pop(0)

    def removerDado(self,valor):
            pos = self.__dados.index(valor)
            for i in range(0,pos+1):
                 self.__dados.pop(0)

    def tamanhoFila(self):
        return len(self.__dados)