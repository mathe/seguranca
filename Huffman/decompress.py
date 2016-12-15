from sys import argv
from huffman import * 
  
def paths(dir):
    dir_file = open(dir)
    len = int(dir_file.readline().replace("\n",""))
    code = dir_file.read()    
    dir_file.close()
    str01 = ""
    for b in code:
        str01 += bin(ord(b))[2:].zfill(8)
    return (len,str01[1:len])
    
def main():
    if len(argv) != 3:
        print("Sao necessarios dois argumentos:")
        print("Endereco do arquivo para ser descompactado.")
        print("Endereco do arquivo para armazenar o conteudo descompactado.")
        return 0
    
    (len_str01,str01) = paths(argv[1])
    trie_file = open("huffman.aux")
    trie = {}
    rt = -1
    for line in trie_file:        
        node = line.replace("\n","").split(":")        
        child = node[1].split(",")
        if rt == -1:
            rt = int(node[0])
        if len(child) == 1:
            trie[int(node[0])] = child[0]
        else:
            trie[int(node[0])] = [int(child[0]),int(child[1])]
    node = rt
    text = ""
    for b in str01:
        node = trie[node][int(b)]
        if len(trie[node]) == 1:
            text += trie[node][0]            
            node = rt             
    dest_file = open(argv[2],"w")
    dest_file.write(text)
    dest_file.close()
    print("O conteudo descompactado foi salvo com sucesso.")
    
if __name__ == "__main__":
    main()