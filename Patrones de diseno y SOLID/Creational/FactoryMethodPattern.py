from __future__ import annotations
from abc import ABC, abstractmethod

#### First part of the example

class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self)->str:
        product = self.factory_method()
        return f"Creator: The same creator {product.operation()}"

class ConcreteCreation1(Creator):
    
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreation2(Creator):
    
    def factory_method(self):
        return ConcreteProduct2()

#### Second part of the example

class Product(ABC):
    
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    
    def operation(self):
        return "Result of the concrete product 1"

class ConcreteProduct2(Product):
    
    def operation(self):
        return "Result of the concrete product 2"

def client_code(creator: Creator)->None:
    print(f"{creator.some_operation()}")
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreation1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreation2())