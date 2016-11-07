from Crypto.Cipher import AES
from sys import argv

def fill16Bytes(text):
	textLen = len(text)
	while textLen % 16 != 0:
		text += 'P'
		textLen += 1
	return text

def myEncrypt(key,text):
	aes = AES.new(key,AES.MODE_CBC,'1111111111111111')
	return aes.encrypt(text)

def myDecrypt(key,text):
	aes2 = AES.new(key,AES.MODE_CBC,'1111111111111111')
	return aes2.decrypt(text)

def main():
	srcKey = open(argv[2]);
	srcText = open(argv[3]);
	destText = open(argv[4],'w');
	
	key = fill16Bytes(srcKey.read())
	text = fill16Bytes(srcText.read())	
	if(argv[1] == "encrypt"):
		destText.write(myEncrypt(key,text))
	elif(argv[1] == "decrypt"):
		destText.write(myDecrypt(key,text))
	srcKey.close()
	srcText.close()
	destText.close()
main()
