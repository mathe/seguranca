from sys import argv

#>>> ord('a')
#97
#>>> chr(97)
#'a'
#>>> chr(ord('a') + 3)
#'d'

def caesar(src,dest,shift):
    text_src = src.read()
    text_dest = ""
    for t in text_src:
        rt = (ord(t)-ord('a')+shift+26) % 26
        text_dest += chr(ord('a')+rt)
    dest.write(text_dest)

def main():
    if len(argv) != 5:
        print("Argumentos incorretos, leia o README.md")
        return 0;
    (src,dest,shift) = open(argv[3],"r"),open(argv[4],"w"),int(argv[2])
    if argv[1] == "-e":
        caesar(src,dest,shift)
    elif argv[1] == "-d":
        caesar(src,dest,(-1)*shift)
    else:
        print("Opcao Invalida")
    src.close()
    dest.close()

if __name__ == "__main__":
    main()
