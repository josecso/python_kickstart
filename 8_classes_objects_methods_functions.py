import csv

###########################################
#                                         #
# Classes, Objects, Methods and Functions #
#                                         #
###########################################



def procura(substring):
    string_found = False
    """ Lookup substring in csv file """
    with open('import.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        # Read into a list
        # csv_import_list=list(csv_reader)
        for row in csv_reader:
            #print(row)
            if substring in row:
                print(f"Found {substring} in row")
                string_found = True
            else:
                print(f"{substring} not found")
    return(string_found)


class Person:
    
    def __init__(self, first_name, age, city):
        self.first_name = first_name
        self.age = age
        self.city = city
        self.fav_movies=[]

    def add_movie(self, movie):
        self.fav_movies.append(movie)

if __name__=='__main__':

    # Create an object of type "Person"
    pessoa=Person('José',47,'Braga')
    print(pessoa)

    # Invoke a function
    string_found = procura(pessoa.first_name)
    print(string_found)

    
    