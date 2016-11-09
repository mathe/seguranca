from sys import argv

#>>> ord('a')
#97
#>>> chr(97)
#'a'
#>>> chr(ord('a') + 3)
#'d'

def vigenere(key,src,dest):
    enc_text = ""
    text = src.read()

    Ki = 0
    key_len = len(key)
    for t in text:
        if Ki == key_len:
            Ki = 0
        enc_text += chr(ord('a') +((key[Ki] + ord(t) - ord('a') + 26) % 26) )
        Ki += 1
    dest.write(enc_text)

def main():
    if len(argv) != 5:
        print("Leia o README.md")
        return 0;
    (key,src,dest) = open(argv[2],"r"),open(argv[3],"r"),open(argv[4],"w")
    key_int = []
    key_text = key.read()
    for k in key_text:
        key_int.append(ord(k)-ord('a'))
    if argv[1] == "-e":
        vigenere(key_int,src,dest)
    elif argv[1] == "-d":
        vigenere([k * (-1) for k in key_int],src,dest)
    else:
        print("Opcao invalida! Leia o README.md")
    key.close()
    src.close()
    dest.close()

if __name__ == "__main__":
    main()
