"""
Demo of type hints
"""
from typing import Optional, Union, Dict, List

a: int = 42
b: float = 1.31
c: bool = True
d: str = "hello world"


def add(x: int, y: int) -> int:
    return x + y


print(add(4, 5))
print(add(6, 7))


def greet(name: Optional[str] = None):
    if not name:
        name = "stranger"
    return "Hello " + name


print(greet("Dennis"))


e: List[int] = [1, 2, 3]
f: Dict[str, float] = {"location": 4.6, "service": 5.0, "quality": 4.9}
g: Union[int, str] = "1"
h: List[Union[int, str]] = [1, 2, "C", "D"]


z: Dict[int, Dict[str, str]] = {1: {"name": "Jane"}, 2: {"name": "John"}}


class MyClass:
    value: int = 42

    def __init__(self) -> None:
        ...

    def add(self, x: int, y: int) -> int:
        return x + y
