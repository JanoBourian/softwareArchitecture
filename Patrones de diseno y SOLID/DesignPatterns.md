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

    - Builder pattern
    - Factory method pattern
    - Prototype patternS
    - Singleton pattern