class Phone:
    def call(self):
        print("Calling...")

class Laptop:
    def call(self):
        print("Video calling...")



def connect(device):
    device.call()

connect(Phone())
connect(Laptop())



class Employee:
    def __init__(self, amt):
        self.__bal = amt  # private

    def draw(self,amt):
        self.__bal-=amt 

    def get_bal(self):
        return self.__bal       

e = Employee(50000)
e.draw(4000)

print(e.get_bal())

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()




