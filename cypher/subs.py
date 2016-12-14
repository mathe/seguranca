from sys import argv

table = {}
inv_table = {}
def load_table(key):
    for tuple in key:        
        t = tuple.split(" ")        
        if len(t[1]) > 1:            
            t[1] = t[1][:1]
        table[t[0]] = t[1]
        inv_table[t[1]] = t[0]

def encrypt(src,dest,key):
    load_table(key)
    dest_txt = ""
    src_text = src.read()
    for c in src_text:
        dest_txt += table[c]
    dest.write(dest_txt)

def decrypt(src,dest,key):
    load_table(key)
    dest_txt = ""
    src_text = src.read()
    for c in src_text:
        dest_txt += inv_table[c]
    dest.write(dest_txt)

def main():
    if len(argv) != 5:
        print("Argumentos incorretos, leia o README.md")
        return 0
    (src,dest,key) = open(argv[3],"r"),open(argv[4],"w"),open(argv[2])    
    if argv[1] == "-e":
        encrypt(src,dest,key)
    elif argv[1] == "-d":
        decrypt(src,dest,key)
    else:
        print("Opcao Invalida")
    src.close()
    dest.close()

if __name__ == "__main__":
    main()