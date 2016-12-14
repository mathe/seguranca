from sys import argv

class Key_Elem:
    idx = -1    #indice original na chave.
    char = '\0'
    def __init__(self,_idx,_char):
        self.idx = _idx
        self.char = _char
    def __lt__(self, o):
        if self.char == o.char:
            return self.idx < o.idx
        return ord(self.char) < ord(o.char)

def sorted_key(key):
    key_txt = key.read()
    len_key_txt = len(key_txt)
    key_elem = []
    for i in range(0,len_key_txt):
        key_elem.append(Key_Elem(i,key_txt[i]))
    return (len_key_txt,sorted(key_elem))

matrix = []
def init_matrix(n):
    for i in range(0,n):
        matrix.append([])

def encrypt(src,dest,key):
    (len_key_txt,sort_key_elem) = sorted_key(key)

    init_matrix(len_key_txt)

    src_txt = src.read()
    len_src_txt = len(src_txt)
    while len_src_txt % len_key_txt:
        src_txt += " "
        len_src_txt += 1

    for i in range(0,len_src_txt):
        matrix[i % len_key_txt].append(src_txt[i])

    dest_txt = ""
    for i in range(0,len_key_txt):
        dest_txt += "".join(matrix[sort_key_elem[i].idx])
    dest.write(dest_txt)

def decrypt(src,dest,key):
    (len_key,sort_key_elem) = sorted_key(key)

    init_matrix(len_key)

    src_txt = src.read()
    len_src_txt = len(src_txt)
    i = 0
    k = 0
    sub = len_src_txt / len_key
    while i < len_src_txt:
        matrix[sort_key_elem[k].idx] = src_txt[i:i+sub]
        k = ( k + 1 ) % len_key
        i += sub

    dest_txt = ""
    for i in range(0,sub):        
        for j in range(0,len_key):
            dest_txt += matrix[j][i]
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
