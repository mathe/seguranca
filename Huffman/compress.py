from sys import argv
from math import * 
from huffman import *

def freq(dir):    
    txt_file = open(argv[1])
    txt = txt_file.read()
    txt_file.close()    
    cnt = {}
    for c in txt:
        cnt[c] = cnt[c] + 1 if c in cnt else 1    
    l = []
    H = 0
    len_txt = len(txt)    
    for s, f in cnt.iteritems():         
        ff = float(f)                   
        H += ff / len_txt * log( len_txt / ff, 256)
        l.append(Node(s,f))
    print(str(H))
    return l
    
def compress(dir,code):    
    text_file = open(dir)
    text = text_file.read()
    text_file.close()
    text_code = ""    
    for c in text:
        text_code += code[c].to01()   
    return "1" + text_code

#01 100 000 01 101 001 111 110

def main():
    if len(argv) != 3:
        print("Sao necessarios dois argumentos:")
        print("Endereco do arquivo para ser compactado.")
        print("Endereco do arquivo para armazenar o conteudo compactado.")
        return 0
    (rt,code) = huffmann(freq(argv[1]))    
    str01 = compress(argv[1],code)            
    dest_file = open(argv[2],"w")
    dest_file.write(str(len(str01)) + "\n")
    dest_file.write(bitarray(str01).tobytes())
    dest_file.close()
    huffman_file = open("huffman.aux","w")
    save(rt,huffman_file)
    print("A arvore para compressao foi armazenada em: huffman.aux")
    huffman_file.close()
    print("O conteudo foi compactado com sucesso.")
    
if __name__ == "__main__":
    main()