from Crypto.Cipher import AES

aes = AES.new('chave de 16 byte',AES.MODE_CBC,'1111111111111111')
mensagem = "mensagem de 16 b"
encript = aes.encrypt(mensagem)

aes2 = AES.new('chave de 16 byte',AES.MODE_CBC,'1111111111111111')
decript = aes2.decrypt(encript)
print(mensagem == decript)
print(decript)
