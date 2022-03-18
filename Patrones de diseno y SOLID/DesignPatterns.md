# Creational
    - Abstract factory pattern
    - Builder pattern
    - Factory method pattern
    - Prototype pattern
    - Singleton pattern

# Structural
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Flyweight
    - Proxy

# Behavioral
    - Chain of responsibility
    - Command
    - Interpreter
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template method
    - Visitor

# Creational

## Abstract factory pattern

Proporciona una interface para crear familias de relaciones u objetos dependientes sin especificar sus clases concretas 

```
class Book:
    pass

class EBook(Book):
    pass 

class PressBook(Book):
    pass

class DoRepository:
    def create_repository(self):
        return Book

class ERepository(DoRepository, Ebook):
    def create_erepository(self):
        return Ebook

class PressRepository(DoRepository, PressBook):
    def create_repository(self):
        return PressBook

```

## Builder pattern

El patrón constructor se utiliza para un manejo de constructores. Separar la construcción de objetos complejos, esto se logra teniendo una única clase que construya objetos.

```

```

## Factory method pattern

Este se utiliza cuando se necesita la creación de objetos con métodos diferentes o más complejos. Se aplica definiendo una interface para crear el objeto, pero las subclases son las que deciden que clase instanciar. Básicamente consiste en no modificar la clase más superior.

    - Prototype patternS
    - Singleton pattern