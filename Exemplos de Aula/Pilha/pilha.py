class Pilha:
    def __init__(self):
        self.__dados = []

    #retorna True se for vazia
    def is_empty(self):
      return len(self.__dados) == 0

    def push(self, novoElem):
        self.__dados.append(novoElem)

    def pop(self):
        if self.is_empty():
            return "Lista Vazia - Não houve Remo"
        return self.__dados.pop()

    def __str__(self):
        return str(self.__dados)

    def topo(self):
      if self.is_empty():
        return ("Pilha vazia")
      else: 
        return self.__dados[-1]

    def __len__(self): 
      return len(self.__dados)

    def esvaziar(self):
        while (len(self.__dados) != 0):
           self.__dados.pop()