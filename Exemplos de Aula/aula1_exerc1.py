def converter_metros_centimetros(metros):
    return (metros*100)

def calcular_ganho(qntdeHoras, valorHora):
    return qntdeHoras*valorHora

#calcular litros
def calcularLitros(metros2):
    return metros2/3

#calcular latas
def calcularLatas(litros):
    qntLatas = int(litros/18)
    if (litros%18 != 0):
        qntLatas = qntLatas+1
    return qntLatas


def main():
    nome = "Alana"
    print(nome)

    #QuestaoD
    #met = int(input("Digite o valor em metros:"))
    #print("O valor em centimetros eh:"+str(converter_metros_centimetros(met)))

    #QuestaoE
    #valorU = float(input("Digite o valor das hora de trabalho:"))
    #quantidadeU = float(input("Digite a quantidade de horas:"))

    #print(calcular_ganho(valorU,quantidadeU))

    #QuestaoF
    #meters = float(input("Digite a quantidade de metros que deseja pintar:"))
    #print(str(calcularLatas(calcularLitros(meters))))

    print (type(int(30)/int(2)))

main()