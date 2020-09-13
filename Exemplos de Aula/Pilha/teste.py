from pilha import Pilha

def main():
    pilhaTeste = Pilha()
    pilhaTeste.push("Teste")
    pilhaTeste.push("Teste2")
    print(pilhaTeste)
    pilhaTeste.pop()
    print(pilhaTeste)

    nome = input("Digite o nome do usuario completo: ")
    for n in nome.split(" "):
        pilhaTeste.push(n.strip())

    print(pilhaTeste)
    pilhaTeste.pop()
    print(pilhaTeste)
    print(pilhaTeste.topo())

    pilhaTeste.esvaziar()


main()