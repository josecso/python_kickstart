##################################################
#                                                #
#        Estrutura de um script em Python        #
#                                                #
##################################################

#BLOCO A
import os
import sys
import datetime
import csv

#BLOCO D
def function_a(input_str):
    print(f'this is function_a printing {input_str}')

#BLOCO B
if __name__=='__main__':
    #BLOCO C
    try:
        pass
        # faz qualquer coisa
    except Exception as ex:
        print(f'Exception found --> {ex}')

    """
    BLOCO A    
        Secção onde são importadas as bibliotecas a utilizar pelo script
        Bibliotecas:
            Standard    - https://docs.python.org/3/library/
            3rd Party   - https://pypi.org   


    BLOCO B
        Convenção que permite que script seja utilizado como "standalone" ou como
        um módulo a importar noutros scripts/programas.

    BLOCO C
        O corpo do script
        try/except --> "exception handling" permite gerir erros (expetáveis e n/
        expetáveis) de forma controlada

    BLOCO D
        Funções e Classes são definidas nesta secção

    """