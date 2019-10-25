class Arvore:
	def __init__(self, c, d = None, e = None):
		self.chave    = c
		self.esquerda = e
		self.direita  = d


#### Parte Estruturada

############# Metodos de Busca #############
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

def buscaLinear(no, chave):
	while no is not None:
		if no.chave == chave:
			return no
		elif chave > no.chave:
			no = no.direita
		else:
			no = no.esquerda
	return None

############ Metodo de Insercao ############
def insere(no, chave):
	if no is None:
		no = Arvore(chave)
	else:
		if chave < no.chave:
			no.esquerda = insere(no.esquerda, chave)   
		else:
			no.direita  = insere(no.direita, chave)  
	return no

######### Acha a Altura da Arvore ##########
def maximo(a, b):
	if a > b:
		return a
	return b

def altura(no):
	if no is None:
		return 0
	return 1 + maximo( altura(no.esquerda), altura(no.direita) )

########### Metodos de Impressao ###########
def preOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	ImprimeArvore += str(no.chave) + ', '
	preOrdem(no.esquerda)
	preOrdem(no.direita)
	
def emOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	emOrdem(no.esquerda)
	ImprimeArvore += str(no.chave) + ', '
	emOrdem(no.direita)

def posOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	posOrdem(no.esquerda)
	posOrdem(no.direita)
	ImprimeArvore += str(no.chave) + ', '


## Main
############################################

arvore = Arvore(3, Arvore(1), Arvore(13) ) # Cria arvore (raiz)
# Insere varios valores na arvore
arvore = insere(arvore, 2)
arvore = insere(arvore, 4)
arvore = insere(arvore, 6)
arvore = insere(arvore, 8)
arvore = insere(arvore, 5)
arvore = insere(arvore, 7)
arvore = insere(arvore, 0)

buscaRecursiva(arvore, 6) # Busca que imprime na propria funcao

if buscaLinear(arvore, 6) is not None: # Retorna o NO ou None se nao encontrou
	print ('valor encontrado\n')
else:
	print ('valor nao encontrado\n')

print ('Altura : %d' % altura(arvore)) # Retorna a altura da arvore (int)

## Chama os metodos de impressao
ImprimeArvore = ""
preOrdem(arvore)
print ("PreOrdem: " + ImprimeArvore + "\n")
ImprimeArvore = ""
emOrdem(arvore)
print ("EmOrdem: " + ImprimeArvore + "\n")
ImprimeArvore = ""
posOrdem(arvore)
print ("PosOrdem: " + ImprimeArvore + "\n")

## Mostra a altura da arvore apos remover os itens
print ('Altura : %d' % altura(arvore))