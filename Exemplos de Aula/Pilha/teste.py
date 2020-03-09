from pilha import Pilha

def main():

    pilhaTeste = Pilha()
    pilhaTeste.push("Teste")
    pilhaTeste.push("Teste2")
    print(pilhaTeste.getPilha())
    pilhaTeste.pop()
    print(pilhaTeste.getPilha())

    nome = input("Digite o nome do usuario completo: ")
    for n in nome.split(" "):
        pilhaTeste.push(n.strip())

    print(pilhaTeste.getPilha())
    pilhaTeste.pop()
    print(pilhaTeste.getPilha())
    print(pilhaTeste.topo())

    pilhaTeste.esvaziar()


main()