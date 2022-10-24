##################################################
#                                                #
#           Utilização de bibliotecas            #
#                                                #
##################################################


# Import completo da biblioteca
import os

# Import de metodos especificos
from os import environ

for item,value in environ.items():
    print(f'{item} : {value}')

# Import de código 
from my_imports import Person
from my_imports import Dog

pessoa=Person('José',47,'Braga')
pessoa.add_movie('Star Wars')
pessoa.add_movie('Bronx Tale')
print(pessoa.fav_movies)

cao=Dog('Nina','Jack Russel')
cao.show_name()

