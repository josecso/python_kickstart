##################################################
#                                                #
#                   Iterables                    #
#                                                #
##################################################


"""
Um iterable é um objeto sobre o qual podemos 'iterar'/percorrer para obter um 
valor distinto a cada iteração
Utilizados para armazenas multiplos itens numa única variável

Tipos de 'Iterables':
---------------------

- list      
- tuple
- dict
- set
- string (*)

    Funções transversais: 
    ---------------------
    sum     - soma os valores de um iterable
    sorted  - ordena os valores de um iterable
    any     - valida se existe um valor qualquer como 'True'
    all     - valida se todos os valores são "True"
    max     - devolve o item com valor máximo
    min     - devolve o item com valor mínimo

"""

# LIST
# Itens ordenados, alteráveis e permitem duplicados
# ocupa mais memória que uma tuple, é mais lenta mas contém mais métodos
my_list_a=[1,22,33,44,55,600,700,8000,90000,0]
my_list_b=['a','b','algum texto',False,True]

#   Métodos:
#   --------
#     append() 	- Adiciona um elemento no final da lista
#     clear()	- Apaga todos os elementos da lista
#     copy()	- Cria uma cópia da lista
#     count()	- Calcula o numero de determinados itens na lista
#     extend()	- Adiciona elementos de outra lista ( ou iterable ) no final 
#                 da lista.
#     index()	- Devolve o index (posiçao) do primeiro elemento da lista com 
#                 determinado valor
#     insert()	- Insere um elemento na lista na posição especificada
#     pop()		- Remove um elmeneto da lista na posição especificada
#     remove()	- Remove um elemento com determinado valor
#     reverse()	- Apresenta a lista no sentido inverso
#     sort()	- Ordena a lista



# TUPLE
# Itens ordenados, n/alteráveis e permitem duplicados
# ocupa menos memória que uma list, é mais rápida mas contém menos métodos
my_tuple_a=('texto',1,'mais texto')

#   Métodos:
#   --------
#     count()   - Devolve o numero de vezes um valor surge na Tuple
#     index()   - Devolve a posição de determinado valor na Tuple




# DICT
# Itens ordenados, alteráveis e n/permitem duplicados
# dados armazenados em formato de "key:value pairs"
# conhecido como "hash" noutras linguagens de programação
# rápido para obter valores fornecendo as chaves 
my_dict_a={'nome':'José','idade':47,'cidade':'Braga'}
my_dict_b={
    'José':{'cidade':47,'cidade':'Braga'},
    'Carlos':{'cidade':47,'cidade':'Braga'},
    }

#   Métodos:
#   --------
#     clear()       - Apaga todos os elementos do dict
#     copy()	    - Cria uma cópia do dict
#     fromkeys()	- Devolve um dict com as chaves e valores especificados
#     get()	        - Obtem o valor da chave especificada
#     items()	    - Devolve uma lista com cada combinação de chave:valor
#     keys()	    - Devolve uma lista com as chaves do dict
#     pop()	        - Remove do dict o item com chave especificada
#     popitem()	    - Remove do dict o ultimo item inserido
#     update()	    - Atualizada o dict com determinado item (chave:valor)
#     values()	    - Devolve uma lista com todos os valores

# SET
# Itens n/ordenados, n/alteráveis e n/permitem duplicados
# itens podem aparecer por ordem diferente em utilizações diferentes
my_set_a={1,22,33,44,55,600,700,8000,90000,0}
my_set_b={'a','b','algum texto',False,True}

set_1={'a','b','c'}
set_2={'a','c','d'}
set_3={'a','ola','adeus'}

#   Métodos:
#   --------
#     add()	                - Adiciona um elemento ao set
#     clear()	            - Apaga todos os elementos do set
#     copy()	            - Cria uma cópia do set
#     difference()	        - Devolve um set com elementos que existem apenas 
#                             no 'set_1'
#     difference_update()	- Remove elementos de um set que estao presentes
#                             noutro set
#     discard()	            - Remove o elemento especificado
#     intersection()	    - Devolve um set com elementos presentes em todos 
#                             os sets
#     intersection_update()	- remove os elementos neste set que nao estao 
#                             presentes nos outros sets
#     isdisjoint()	        - Boolean. Identifica se 2 sets se intersetam
#     issubset()	        - Boolean. Identifica se este set está presente 
#                             noutro set
#     issuperset()	        - Boolean. Identifica se este set contem outro set
#     pop()	                - Remove um elemento aleatório do set e devolve o 
#                             valor do mesmo
#     remove()	            - Remove o elemento especificado do set 
#                             ( ** will raise exception )
#     union()	            - Devolve um set que é a junção de 2 sets (exclui 
#                             duplicados)
#     update()	            - Atualiza o set com valores de outros sets ( ou 
#                             iterables )

#Alguns exercicios:

set_1.difference(set_2)
set_3.remove('ola')
set_1.intersect(set_2,set_3)
set_1.intersect_update(set_2,set_3)
set_3.remove('adeus')

