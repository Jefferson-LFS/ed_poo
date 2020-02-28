'''
#Questao matriz
def imprimir(matriz2):
    print()
    for i in range(len(matriz2)):
        for j in range(len(matriz2[i])):
            print(matriz2[i][j], end=' ')
        print()


def main():
   matriz = [[39,14,27],[21,83,92],[31,12,43]]

   imprimir(matriz)

   for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] *= 7

   imprimir(matriz)

main()
'''

'''
def main():
  matriz = [[39,14,27],[21,83,92],[31,12,43]]

  print(matriz)

  for i in matriz:
      i.remove(i[-1])
  
  print(matriz)

main()

'''

'''
def imprimir(matriz2):
    print()
    for i in range(len(matriz2)):
        for j in range(len(matriz2[i])):
            print(matriz2[i][j], end=' ')
        print()


def main():
  matriz = [
  ["Bruna", "123131443"],
  ["Alberto", "32141241"],
  ["Filipe","9474945"]
  ]

  matriz.append(["Eduardo"])
  matriz.append(["Thiago", "2342342334"])
  matriz[0].append("10.0")
  imprimir(matriz)
  
  matriz[3].append("11111111")
  imprimir(matriz)

main()
'''

def main():
  matriz = [[1,2,3,4],[5,6,7,8]]

  print(matriz)

  novonum = int(input("Digite o número a ser inserido: "))

  for i in matriz:
    i.append(novonum)

  print(matriz)


main()
