from typing import TypeVar, Generic

# Define a generic type T
T = TypeVar("T")


# A generic class Stack that operates on elements of type T
class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0


# Creating a stack of integers
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())  # Output: 3

# Creating a stack of strings
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # Output: world
