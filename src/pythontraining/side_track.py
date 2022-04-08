

class Precipitation:
    def __init__(self, name, measurements):
        self.name = name
        self.measurements = measurements

    def drop_duplicates(self):
        self.measurements = list(set(self.measurements))


OTT = Precipitation("OTT", [1, 1, 1])
LEN = Precipitation("LEN", [2, 2, 2])


all_data = [OTT, LEN]

for precipitation in all_data:
    precipitation.drop_duplicates()
    print(precipitation.name, precipitation.measurements)


print()


def add_something_to(my_list):
    my_list.append("new")
    my_list = [4, 5, 6]
    print("within the function", my_list)    # -> 4, 5, 6


my_list = [1, 2, 3]
add_something_to(my_list)
print("outside the function", my_list)       # -> 1, 2, 3, new

"""
Immutable:
- integers
- floats
- strings
- boolean
- tuples

Mutable:
- dictionaries
- lists
- sets
"""