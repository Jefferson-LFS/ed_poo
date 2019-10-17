def main():
    dicionario = {"Ricardo":["10/02","End2"], "Samir":["20/08", "End1"], "Amanda":["27/12","End3"]}
    #print(dicionario)

    for valor in dicionario.values():
       print(valor)
    
    for chave in dicionario.keys():
       print(chave)

    dicionario.pop("Ricardo")
    dicionario["Amanda"] = None
    print(dicionario)

main()