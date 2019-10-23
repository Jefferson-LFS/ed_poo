class Arvore:
    def __init__(self, c, d = None, e = None):
        self.chave=c
        self.esquerda = e
        self.direita = d


##Parte Estruturada
def insere(no, chave):
	if no is None:
		no = Arvore(chave)
	else:
		if chave < no.chave:
			no.esquerda = insere(no.esquerda, chave)   
		else:
			no.direita  = insere(no.direita, chave)  
	return no

def buscaLinear(no, chave):
	while no is not None:
		if no.chave == chave:
			return no
		elif chave > no.chave:
			no = no.direita
		else:
			no = no.esquerda
	return None

def buscaRecursiva(no, chave):
	if no is None:
		print (str(chave) + ' nao foi encontrado na arvore\n')
		return None
	if no.chave == chave:
		print (str(chave) + ' foi encontrado na arvore\n')
		return no
	if chave > no.chave:
		buscaRecursiva(no.direita, chave)
	else:
		buscaRecursiva(no.esquerda, chave)


arvore = Arvore(3, None, Arvore(1))
arvore = insere(arvore, 2)
arvore = insere(arvore, 4)
arvore = insere(arvore, 6)
arvore = insere(arvore, 7)

buscaRecursiva(arvore, 5)
buscaRecursiva(arvore, 1)