from Crypto.Cipher import AES
from sys import argv

def fill16Bytes(text):
	textLen = len(text)
	while textLen % 16 != 0:
		text += 'P'
		textLen += 1
	return text

def myEncrypt(text,key):
	aes = AES.new(key,AES.MODE_CBC,'1111111111111111')
	return aes.encrypt(text)

def myDecrypt(text,key):
	aes2 = AES.new(key,AES.MODE_CBC,'1111111111111111')
	return aes2.decrypt(encript)

def main():
	argc = len(argv);
	if argc != 4:
		print("Entrada incorreta leia o readme.")
		return

	if(argv[1] == "encrypt"):
		print("encriptar")
	elif(argv[1] == "decrypt"):
		print("decriptar")
	else:
		print("Opcao invalida leia o readme.");
main()
