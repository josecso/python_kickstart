##################################################
#                                                #
#        Exemplo de um Script a importar         #
#                                                #
##################################################

class Person:
    
    def __init__(self, first_name, age, city):
        """
        Create a Person object and set the first_name, age and city.
        Initializes an empty list of favourite movies
        """
        self.first_name = first_name
        self.age = age
        self.city = city
        self.fav_movies=[]

    def add_movie(self, movie):
        self.fav_movies.append(movie)

class Dog:
    def __init__(self, name, breed):
        """
        Create a Dog object and set the name and breed.
        """
        self.name = name
        self.breed = breed
    
    def show_name(self):
        print(f"\n\nThe dog's name is {self.name}\n\n")


if __name__=="__main__":
    print("Nada")