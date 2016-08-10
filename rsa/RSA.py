from Crypto.PublicKey import RSA

def newPair():
	global rsa
	rsa = RSA.generate(2048)
	return rsa.publickey().exportKey("PEM"),rsa.exportKey("PEM")

def myEncrypt(pathIn,pathOut):
	return rsa.encrypt(open(path).read(),None)

def myDecrypt(path):
	return rsa.decrypt(open(path).read())

def main():
	while 1:
		op = int(raw_input("Digite 1 para gerar um novo par de chaves.\n" +
						   "Digite 2 para mostrar a chave publica.\n" +
				 		   "Digite 3 para encryptar um texto.\n" +
						   "Digite 4 para decryptar um texto.\n"))
		if op == 1:
			keys = newPair()
		elif op == 2:
			print(keys[0])
		elif op == 3:
			myEncrypt(raw_input("Caminho para o arquivo com o texto:"))
		else:
			pathKey = raw_input("Caminho para o arquivo com a chave publica:")
			pathText = raw_input("Caminho para o arquivo com o texto:")
			myDecrypt(pathKey,pathText)
main()
