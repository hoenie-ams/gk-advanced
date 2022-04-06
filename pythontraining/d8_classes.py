"""
Demo of classes
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_object = Rectangle(length=10, width=20)
print(my_object)
print(my_object.width)
print(my_object.area())


# Another example
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        return f"{self.owner} has EUR {self.balance}"


account_jens = BankAccount(12345, "Jens", 0)
account_jens.deposit(100)
print(account_jens.display_balance())


class Base:
    pass


class Derived(Base):
    pass


class Vehicle:
    description = "This is a vehicle"

    def brake(self):
        return "Stopping"

    def drive(self):
        return "Driving"


class Car(Vehicle):
    def __init__(self, color):
        self.color = color


class Truck(Vehicle):
    wheels = 8

    def drive(self):
        return "Driving the truck!!"


car = Car("red")
print(car.description)
print(car.color)
print(car.drive())
print(car.brake())

truck = Truck()
print(truck.drive())
