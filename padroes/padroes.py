from sys import argv

def calc_patt(word):
    cnt = 0
    patt = ""
    check = {}
    for c in word:
        if c not in check:            
            check[c] = cnt
            cnt += 1
        patt += str(check[c])
    return patt

def main():
    if len(argv) != 3:
        print("Argumentos incorretos, leia o README.md")
        return 0
    (words_file,patt_file) = open(argv[1],"r"),open(argv[2],"w")        
    for line in words_file.read().split("\n"):
        for word in line.split(" "):
            if len(word) == 0:
                continue            
            patt_file.write(word + " -> " + calc_patt(word) + "\n")        
    patt_file.close()
    words_file.close()    

if __name__ == "__main__":
    main()