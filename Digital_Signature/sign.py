from Crypto.PublicKey import RSA
from hashlib import sha256
from sys import argv

SEPARATOR = '\t\n'

def sign(file):
    rsa = RSA.generate(2048)
    content = file.read()
    hash_content = sha256(content).hexdigest()
    pub_key = rsa.publickey().exportKey("PEM")
    hash_pub_key = sha256(pub_key).hexdigest()
    content += SEPARATOR+rsa.encrypt(hash_content,None)[0]
    content += SEPARATOR+hash_pub_key
    content += SEPARATOR+pub_key
    open("content_signature.txt",'w').write(content)
    print("A assinatura digital do conteudo esta em content_signature.txt")

def check(file):
    sign = file.read()
    pieces = sign.split(SEPARATOR)
    if len(pieces) == 4:
        pubKey = RSA.importKey(pieces[3])
        if sha256(pieces[3]).hexdigest() == pieces[2]:
            if pubKey.encrypt(sha256(pieces[0]).hexdigest(),None)[0] == pieces[1]:
                print("Assinatura correta!")
                return 0
    print("Assinatura incorreta!")

def main():
    if len(argv) != 3:
        print("Leia o arquivo README.md")
        return 0
    if argv[1] == '-s':
        sign(open(argv[2],"r"))
    elif argv[1] == '-c':
        check(open(argv[2]))
    else:
        print("Leia o arquivo README.md")


if __name__ == "__main__":
    main()
