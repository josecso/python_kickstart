##################################################
#                                                #
#            Variables and Data Types            #
#                                                #
##################################################


"""
Variável:
=========
- Espaço dedicado em memória para armazenar valores
- Não necessita de ser declarada/inicializada antes de ser atribuido valor
    De acordo com PEP8:
    - Deverá começar com uma letra
    - Não deverá começar com um numero
    - combinação de (A-Z, a-z, 0-9)
    - Não pode conter espaços e certos carateres (*,\,/,#)
    - São "case-sensitive"
    - "Upper-case" --> Varíavel de valor fixo

Data Types:
===========
Numeric:
    - integer   - Números inteiros
    - float     - Números decimais

Text:
    - string    - Numeros, letras e carateres ( entre ' ou " )    

Mapping:
    - dictionary - conjunto de chaves e valores

Boolean:
    - bool      - True ou False

Sequence:
    - list      - lista de valores (permite repetidos)
    - set       - lista de valores (nao permite repetidos)

"""

"""
Alguns métodos disponiveis para strings:
----------------------------------------

upper() --> converte string para maiúsculas
lower() --> converte string para minusculas
capitalize() --> coloca primeira letra da string como maiuscula e restante minusculo
title() --> coloca primeira letra de todas as palavras como maiúscula
strip() --> remove espaço no incio e fim
isalpha() --> valida se a string contem apenas letras *
isdigit() --> valida se a string contem apenas digitos *
startswith(char) --> valida se a string começa por determinado caratér ou palavra *
endswith(char) --> valida se a string termina por determinado caratér ou palavra *
find(substring,start,end) --> devolve posição de determinado texto dentro da string 
replace(old,new) --> substitui determinado texto numa string
split(delimeter) --> cria uma lista a partir de uma string
index(char) --> devolve a posição da primeira ocorrência de determinado carater
count(char) --> numero de vezes determinado carater surge na string

Nota1:
* devolve valor boolean

Nota2:
R-Strings ( Raw Strings ) - utilizadas quando é necessário incluir "escape 
characters" como "\"
exemplo: 
a="ola\ncomo\nestá?"
print(a)
a=r"ola\ncomo\nestá?"
print(a)


Anexar strings:
----------------------------------------
"""
str_a="Benvindos"
str_b="a uma breve"
str_c="introdução ao Python"

#   + operator
str_final_a=str_a+" "+str_b+" "+str_c

#   join() method
str_final_b=" ".join([str_a,str_b,str_c])

#   % operator
str_final_c="%s %s %s" % (str_a,str_b,str_c)

#   format() function
str_final_d="{} {} {}".format(str_a, str_b, str_c)

#   f-string
str_final_e=f"{str_a} {str_b} {str_c}"

print("fim")


