from fila import Fila

fila1 = Fila()
fila1.inserirDado(0)
fila1.inserirDado(1)
fila1.inserirDado(2)
print(fila1.getFila())

fila1.remover()
print(fila1.getFila())
fila1.removerDado(2)

tam = fila1.tamanhoFila()
if (tam != 0):
    print(fila1.getFila())
else:
    print("Lista Vazia")
