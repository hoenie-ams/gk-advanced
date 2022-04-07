"""
Show difference between class variables and instance variables
"""


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def say_hello(self):
        return f"{self.name} says hello!"

    @classmethod
    def display_population_count(cls):
        return f"The total population is {cls.count}"


print(Person.display_population_count())

joris = Person("Joris")
evans = Person("Evans")

# Instance var
print(joris.name)
print(joris.say_hello())
print(joris.display_population_count())


# Class var vs instance
print(Person.count)
print(joris.count)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.split("-")
        return cls(year, month, day)


d1 = Date(2015, 1, 3)
d2 = Date.from_string("2022-04-06")
# d3 = Date.from_dict({"year": 2022, "month": 4, "day": 6})
