"""
.. include:: ../../README.md
"""

def say_hello(name:str) -> str:
    """This functions print hello"""
    return f"Hello {name}"

class Greeting:

    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}"

if __name__ == "__main__":
    print("Hello Python")
    print(say_hello("John Doe"))

    greeting = Greeting("Jane Doe")
    print(greeting.say_hello())
