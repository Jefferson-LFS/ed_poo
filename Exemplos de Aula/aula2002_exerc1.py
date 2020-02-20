'''
#Questao I
def verificar_sinal(num):
    if num >= 0:
       return "Número positivo!"
    else:
       return "Número negativo!"

def main():
    numero = int(input("Digite um número: "))
    print (verificar_sinal(numero))

main()
'''

'''
#Questao J

def main():
    letra = input("Digite uma letra: ")

    if letra == "M":
        print("Masculino")
    elif letra == "F":
        print("Feminino")
    else:
        print("Sem Gênero")

main()
'''

'''
#Questao K
def main():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media == 10:
        print("Aprovado com Distinção!")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

main()
'''

'''

#Questao L
def main():
    nome1 = input("Digite o nome do 1o produto: ")
    preco1 = float(input("Digite o preço do 1o produto: "))
    nome2 = input("Digite o nome do 2o produto: ")
    preco2 = float(input("Digite o preço do 2o produto: "))
    nome3 = input("Digite o nome do 3o produto: ")
    preco3 = float(input("Digite o preço do 3o produto: "))

    if (preco1 < preco2) and (preco1 < preco3):
        print("Compre o",nome1)
    elif (preco2 < preco1) and (preco2 < preco3):
        print("Compre o", nome2)
    else:
        print("Compre o", nome3)

main()
'''

'''
#Questao M
def main():
    lista = []

    for i in range(0,3):
        num = int(input("Digite um número: "))
        lista.append(num)

    lista.sort()
    print(lista)

main()
'''

'''

#Questao N
def main():
    notas = []

    quantidade_notas = int(input("Quantas notas deseja cadastrar? "))

    for i in range(1,quantidade_notas+1):
        notas.append(int(input(f"Digite a nota numero {i}: ")))

    soma = 0.0
    for nota in notas:
        soma += nota

    media = soma / quantidade_notas

    print("Média = ",media)

main()
'''

'''
#Questao O
def main():
    inicio = int(input("Início da sequência: "))
    termino = int(input("Término da sequência: "))

    for i in range(inicio, termino+1):
        if i < termino:
            print(i ** 2, end=", ")
        else:
            print(i ** 2, end="\n")

main()
'''

'''
#Questao P
#melhorem e transforme em uma função
def main():
    entrada = int(input("Fatorial de qual valor? "))

    fatorial = 1
    for i in range(1,entrada+1):
        fatorial *= i #fatorial = fatorial * i
        if i < entrada:
            print(f"{i}", end=" x ")
        else:
            print(i, end=" = ")

    print(fatorial)

main()
'''

'''
#QUESTAO Q
def main():
    numero = int(input("Gerar a tabuada para qual número? "))

    for i in range(1,10):
        print(f"{numero} x {i} = {i*numero}")
main()
'''

'''
#Questao R
def palindromo(entrada):
    p = False
    for i in range(0,len(entrada)):
        for j in reversed(range(0, len(entrada))):
            p = entrada[i] == entrada[j]
    return p


def main():
    entrada = input("Digite a entrada: ")

    if palindromo(entrada):
        print("É palíndromo!")
    else:
        print("Não é palíndromo")

main()

'''

'''
#Questao S
def triangulo_retangulo(num1, num2, num3):
    return (num1 ** 2) == (num2 ** 2 + num3 ** 2)

def main():
    hip = int(input("Digite a hipotenusa: "))
    c1 = int(input("Digite um cateto: "))
    c2 = int(input("Digite o outro cateto: "))
    if triangulo_retangulo(hip, c1, c2):
        print("É um triangulo retangulo")
    else:
        print("Não é um triangulo retangulo")
main()
## 5, 4, 3

'''
