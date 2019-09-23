# Program the prints the oldest of three dogs

class Dog:
    
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.full = name + " "+ "is " + str(age) + " year's"
        
     
        
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
johnny = Dog("Johnny", 8)

def get_biggest_number(*args):
    return max(args)
    
print("The oldest dog is {} years old.".format(
    get_biggest_number(philo.age, mikey.age, johnny.age)))