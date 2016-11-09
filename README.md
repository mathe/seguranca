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

Caesar:
Para criptografar:
caesar.py -e tamanho_shift origem.txt destino.txt

Para decriptografar:
caesar.py -d tamanho_shift origem.txt destino.txt

Vigenere:
Para criptografar:
vigenere.py -e key.txt origem.txt destino.txt

Para decriptografar:
vigenere.py -d key.txt origem.txt destino.txt
