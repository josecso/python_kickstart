import random
import os
from stat import ST_CTIME

################################
#                              #
#    Trabalhar com ficheiros   #
#                              #
################################

if __name__=='__main__':
    
    #Ler conteudos de um ficheiro

    with open('file_to_read.txt','r') as file:
        data=file.read()

    # Gerar uma lista com as linhas de um texto
    list_1=data.splitlines()

    # Escrever para um ficheiro
    with open('output.txt','w') as file_out:
        for i in range(1,1000):
            file_out.write(f'Palavra #{i}\n')

    # Obter ficheiros ( e modified time) num diretorio
    with os.scandir(r'c:\temp') as files:
        for f in files:
            print(f.name,f.stat().st_mtime)
