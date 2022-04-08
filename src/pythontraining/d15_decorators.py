"""
Demo of decorators
"""


def say_hello():
    print("Hello, how are you?")


# 1. Functions as objects
greet = say_hello
# greet()


# 2. Functions as arguments
def my_simple_decorator(func):
    print("Decorating the function")
    func()


# my_simple_decorator(say_hello)


def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


say_hello = my_decorator(say_hello)
# say_hello()


@my_decorator
def say_hello():
    print("Hello, how are you?")

say_hello()
