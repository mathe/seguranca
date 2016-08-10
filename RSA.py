from Crypto.PublicKey import RSA

def main():
	rsa = RSA.generate(2048)
	while 1:
		op = int(raw_input("\nDigite 1 para receber uma chave publica.\n" +
						   "Digite 2 para criptografar(com a chave publica) um texto.\n" +
						   "Digite 3 para decriptografar(com a chave privada) um texto.\n" ))
		if op == 1:
			path = raw_input("Digite o local para a chave publica: ")
			open(path,'w').write(rsa.publickey().exportKey("PEM"))
		elif op == 2:
			keyPath = raw_input("Digite o local da chave publica: ")
			textSrc = raw_input("Digite o local do texto a ser criptografado: ")
			textDest = raw_input("Digite o local para o texto criptografado: ")
			pubKey = RSA.importKey(open(keyPath).read())
			text = open(textSrc).read()
			open(textDest,'w').write(pubKey.encrypt(text,None)[0])
		else:
			textSrc = raw_input("Digite o local do texto a ser decriptografado: ")
			textDest = raw_input("Digite o local para o texto decriptografado: ")
			text = open(textSrc).read()
			open(textDest,'w').write(rsa.decrypt(text))
main()
