'''
Example on classes.

Super class with properties and Methods(Functions)
Sub classes inhereting from Super class

Use of objects to print out information
'''

class Vehicle():
    has_wheel = True
    runs_on_fuel = True

    def honk(self):
        print("Honk! Honk!")

class Car(Vehicle):
    number_of_wheels = 4

class Train(Vehicle):
    number_of_wheels = 108
    
vehicle = Vehicle()
print(vehicle.runs_on_fuel)

print(Vehicle.honk)

car = Car()
print(car.number_of_wheels)

train = Train()
print(train.number_of_wheels)