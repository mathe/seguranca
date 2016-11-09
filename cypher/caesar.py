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
        rt = (ord(t)-ord('a')+shift+256) % 256
        text_dest += chr(ord('a')+rt)
    dest.write(text_dest)

def main():
    if len(argv) != 4:
        print("Argumentos incorretos, leia o README.md")
        return 0;
    (src,dest,shift) = open(argv[2],"r"),open(argv[3],"w"),int(argv[1])
    caesar(src,dest,shift)
    src.close()
    dest.close()

if __name__ == "__main__":
    main()
