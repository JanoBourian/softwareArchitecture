from curses.ascii import SI


class SingletonMeta(type):
    
    _instance = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

class Singleton(metaclass = SingletonMeta):
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    
    if id(s1) == id(s2):
        print("Singleton works")
    else: 
        print("Singleton failed")