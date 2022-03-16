from __future__ import annotations
from abc import ABC, abstractmethod


"""
General Abstract Factory
"""

class AbstractFactory(ABC):
    @abstractmethod
    def create_producto_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_producto_b(self) -> AbstractProductoB:
        pass

"""
Concrete Factories
"""

class ConcreteFactory1(AbstractFactory):
    def create_producto_a(self)-> AbstractProductA:
        return ConcreteProductA1()
    
    def create_producto_b(self)-> AbstractProductoB:
        return ConcreteProductoB1()

class ConcreteFactory2(AbstractFactory):
    def create_producto_a(self)-> AbstractProductA:
        return ConcreteProductA2()
    
    def create_producto_b(self)-> AbstractProductoB:
        return ConcreteProductoB1()

""" 
Abstract products
"""

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self)->str:
        pass

class AbstractProductoB(ABC):
    @abstractmethod
    def useful_function_b(self)->str:
        pass
    
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

""" 
Concrete products
"""

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

class ConcreteProductoB1(AbstractProductoB):
    def useful_function_b(self) -> str:
        return "The result of the product B1"

""" 
Client code
"""

def client_code(factory:AbstractFactory)-> None:
    product_a = factory.create_producto_a()
    print(product_a.useful_function_a())

""" 
Implementation
"""

if __name__ == "__main__":
    client_code(ConcreteFactory1())