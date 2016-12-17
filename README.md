# seguranca
Repositório da disciplina de Segurança e Auditoria de Sistemas

Diffie Hellman:
O menu do programa é o suficiente para utilizá-lo.

AES:

Para criptografar:
python AES.py encrypt arquivo_com_chave arquivo_com_texto arquivo_para_saida

Para descriptografar:
python AES.py decrypt arquivo_com_chave arquivo_com_texto_criptografado arquivo_para_saida

RSA: É só ler o menu.

Digital_Signature:

-s <local_do_arquivo_com_conteudo>
-c <local_do_arquivo_com_assinatura_para_ser_validada>  

BO: É somente necessário a execução do servidor e do cliente.

cypher:
O arquivo origem.txt deve conter o texto a ser criptografado/decriptografado.
O arquivo destino.txt será onde o texto criptografado/decriptografado será guardado.

Caesar:
Para criptografar:
caesar.py -e tamanho_shift origem.txt destino.txt

Para decriptografar:
tamanho_do_shift deve ser o tamanho do shift em que o texto foi criptografado.
caesar.py -d tamanho_shift origem.txt destino.txt

Vigenere:
Para criptografar:
vigenere.py -e key.txt origem.txt destino.txt

Para decriptografar:
vigenere.py -d key.txt origem.txt destino.txt

Transposicao:
Para criptografar:
vigenere.py -e key.txt origem.txt destino.txt

Para decriptografar:
vigenere.py -d key.txt origem.txt destino.txt

Substituição:
O arquivo key.txt deve ser conter 256 tuplas no formato:
A B
onde A e B são símbolos do alfabeto, cada tupla indica que o símbolo A
será substituido pelo símbolo B.

Para criptografar:
vigenere.py -e key.txt origem.txt destino.txt

Para decriptografar:
vigenere.py -d key.txt origem.txt destino.txt

Padroes:
palavras.txt deve ser o arquivo de texto contendo as palavras. As palavras 
devem ser separadas por espaço ou quebra de linha.
padroes.txt deve ser o arquivo de texto contendo os padrões de cada palavra.
padroes.py palavras.txt padroes.txt