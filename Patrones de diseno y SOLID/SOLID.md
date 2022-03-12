# SOLID

- S : Single responsibility principle
- O : Open / Closed principle
- L : Liskov susbstitution principle
- I : Interface segregation principle
- D : Dependency Inversion principle 

## S : Single responsibility principle

- En un sistema bien diseñado cada clase tiene una responsabilidad. Ejemplo: una clase no debería recuperar, formatear y procesar información, sólo debería procesar la información sin saber cómo se recupera dicha información ni cómo se formatea. La clase "recuperadora" se puede extender para convertirse en un manejador de información y la clase "formateadora" se puede extender para devolver todos los formatos disponibles. 

```
class Reporte:
    def recuperar_informacion(self):
        # proceso 

    def formatear_documento(self):
        # proceso
    
    def ajustar_informacion(self):
        # proceso
```

```
class Recuperador:
    def recuperar_informacion(self):
        # proceso 

class Formateador:
    def formatear_documento(self):
        # proceso

class Reporte:
    informacion = Recuperador.recuperar_informacion()

    def ajustar_informacion(self):
        # proceso
        formato = Formateador.formatear_documento()    
```

## O : Open / Closed principle

- Clases, modulos, funciones, etcétera deben estar abiertas para la extensión pero cerradas para la modificación. Debemos analizar qué metodos corresponden a cada clase. Un Pintor va a utilizar diversos métodos para pintar diversos tipos de objetos, el pintor se debe limitar a "Pintar" y es responsabilidad de cada objeto el cómo se va a pintar. 

```
class Pintor:
    def pintar(self, objeto:Objeto):
        objeto.pintar()

class Objeto1:
    def pintar(self):
        # Especificaciones de cómo se debe pintar

class Objeto2:
    def pintar(self):
        # Especificaciones de cómo se debe pintar
```

Ahora bien, debemos dejar un punto abierto dentro de la clase para que se modifiquen en la implementación, como se hace con el método \_\_str()\_\_ al sobreescribir métodos. Ejemplo ilustrativo:

```
class Alumnos:
    def retornar_aprobados(self)
        # proceso
        return self.ordenamiento(lista)
    
    def ordenamiento(self, lista):
        # proceso
        # aquí se define el tipo de ordenamiento 
        return lista

class AlumnosPrimaria(Alumnos):
    def ordenamiento(self):
        # proceso de sobrescritura del método
    
```

## L : Liskov substitution principle

- Supongamos una clase T superior y una clase S derivada de T. Para que este principio se pueda dar se debe cumplir que los métodos y propiedades de T deben estar contenidos en S. 

```
class Pato:
    def parpar(self): 
        print "Cuac!"
    def plumas(self): 
        print "El pato tiene plumas blancas y grises."
 
class Persona:
    def parpar(self):
        print "La persona imita el sonido de un pato."
    def plumas(self): 
        print "La persona toma una pluma del suelo y la muestra."
 
def en_el_bosque(pato):
    pato.parpar()
    pato.plumas()
 
def juego():
    donald = Pato()
    juan = Persona()
    en_el_bosque(donald)
    en_el_bosque(juan)

juego()
```

## I : Interface segregation principle

- Los clientes no deben ser forzados a depender de métodos que ellos no usa. 

```
class Comunicador:

    def encriptar_mensaje(self):
        # proceso

    def enviar_sms(self):
        # proceso
    
    def enviar_wa(self):
        # proceso
```

```
class Encriptador:
    def encriptar_mensaje(self):
        # proceso

class Comunicador:
    def enviar_sms(self):
        # proceso
    
    def enviar_wa(self):
        # proceso

class Cliente1(Comunicador, Encriptador):
    # métodos

class Cliente2(Comunicador):
    # métodos 
```

## D : Dependency inversion principle

- Las dependencias tradicionalmente se descomponen en tareas muy simples. Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones y las abstracciones no deben depender de los detalles, los detalles deben depender de las abstracciones.

```
- Lógica de negocio
- Operaciones básicas
- Accesos a información y Base de datos.
```

```
- Lógica de negocio : API de Operaciones básicas
- Operaciones básicas : API de accesos a información 
- Accesos a información y Base de datos.
```