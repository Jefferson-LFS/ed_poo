class Pilha:
    def __init__(self):
        self.__dados = []

    def getPilha(self):
        return self.__dados

    def push(self, novoElem):
        self.__dados.append(novoElem)

    def pop(self):
        self.__dados.pop()

    def topo(self):
        return (self.__dados[len(self.__dados) - 1])

    def esvaziar(self):
        while (len(self.__dados) != 0):
           self.__dados.pop()