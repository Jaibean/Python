#
# Python Ver:   3.9
#
# Author:       Jaimie Bertoli
#
# Purpose:      Create two classes that inherit from another class.
#               1. Each child should have at least two of their own attributes.
#               2. The parent class should have at least one method (function).
#               3. Both child classes should utilize polymorphism on the parent class method.
#               4. Add comments throughout your Python explaining your code.


#Parent class
class Vehicle:
    make = 'No Make Provided'
    model =  ' '
    year = ' '

    def getMoreInfo(self):
        print(self.make)

# Child class   
class Bikes(Vehicle):
    gear = 'fixed'
    motar = False

    def getMoreInfo(self):
        print(self.gear)
        
#Child class
class Cars(Vehicle):
    car_type = 'SUV'
    engine_type = 'gas'

    def getMoreInfo(self):
        print(self.car_type)

# This code invokes the methods inside each class

Vehicle1 = Vehicle()
Vehicle1.getMoreInfo()

Bike1 = Bikes()
Bike1.getMoreInfo()

Car1 = Cars()
Car1.getMoreInfo()
