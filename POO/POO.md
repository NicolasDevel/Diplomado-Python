
# Programación Orientada a Objetos (POO) en Python

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que organiza el código mediante el uso de objetos. Cada objeto es una instancia de una **clase**, y las clases son moldes que definen las propiedades y el comportamiento de esos objetos. Python es un lenguaje que soporta POO de manera completa, lo que facilita la creación de programas más estructurados, reutilizables y fáciles de mantener.

## Conceptos Clave de la POO

### 1. **Clases**
Una clase es una plantilla para crear objetos. Define los atributos y métodos que los objetos de esa clase tendrán. En otras palabras, las clases son los planos de los objetos.

#### Ejemplo:
```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")
```

- **`__init__`** es un método especial llamado constructor que se llama cuando se crea un nuevo objeto.
- **`self`** hace referencia al objeto actual que está siendo creado o manipulado.

### 2. **Objetos**
Un objeto es una instancia de una clase. Se crea utilizando la clase como plantilla y se puede acceder a sus atributos y métodos.

#### Ejemplo:
```python
mi_perro = Perro("Rex", 3)
mi_perro.hablar()  # Imprime: Rex dice: ¡Guau!
```

### 3. **Métodos**
Los métodos son funciones definidas dentro de una clase que definen el comportamiento de los objetos. Los métodos pueden acceder y modificar los atributos de los objetos.

#### Ejemplo:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y tengo {self.edad} años.")
```

### 4. **Herencia**
La herencia es un mecanismo que permite a una clase derivada (hija) heredar atributos y métodos de una clase base (padre). Esto permite la reutilización de código y facilita la extensión del comportamiento.

#### Ejemplo:
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class Gato(Animal):  # Gato hereda de Animal
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")
```

- La clase `Gato` hereda el método `dormir` de la clase `Animal`, pero también puede agregar métodos propios, como `maullar`.

### 5. **Polimorfismo**
El polimorfismo es la capacidad de un objeto de tomar muchas formas. En la POO, esto significa que un mismo método puede tener diferentes comportamientos dependiendo de la clase del objeto que lo invoque.

#### Ejemplo:
```python
class Vehiculo:
    def mover(self):
        print("El vehículo se mueve")

class Coche(Vehiculo):
    def mover(self):
        print("El coche está conduciendo")

class Barco(Vehiculo):
    def mover(self):
        print("El barco está navegando")

def iniciar_mover(vehiculo):
    vehiculo.mover()

coche = Coche()
barco = Barco()

iniciar_mover(coche)  # El coche se mueve
iniciar_mover(barco)  # El barco se mueve
```

### 6. **Encapsulamiento**
El encapsulamiento es el principio de ocultar los detalles internos de una clase y exponer solo lo necesario. En Python, esto se hace mediante convenciones de nombres como `_` (protegido) y `__` (privado).

#### Ejemplo:
```python
class Banco:
    def __init__(self):
        self.__saldo = 1000  # Atributo privado

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

banco = Banco()
banco.depositar(500)
print(banco.obtener_saldo())  # Acceder al saldo mediante un método público
```

### 7. **Abstracción**
La abstracción es el proceso de ocultar los detalles de implementación y mostrar solo la funcionalidad relevante de un objeto. Esto se logra mediante la creación de interfaces y clases abstractas, que proporcionan una visión simplificada del objeto.

## Ventajas de la POO

1. **Reutilización de código**: Las clases pueden ser reutilizadas en diferentes programas.
2. **Escalabilidad**: Es más fácil extender y modificar un sistema orientado a objetos.
3. **Mantenimiento**: Es más fácil mantener y actualizar el código debido a la separación de responsabilidades en las clases.
4. **Modularidad**: Cada objeto es autónomo y realiza tareas específicas, lo que mejora la organización del código.

## Conclusión
La Programación Orientada a Objetos es una técnica poderosa para crear aplicaciones estructuradas y reutilizables. Python hace que implementar POO sea simple y eficiente, permitiendo crear soluciones robustas y escalables. La comprensión de conceptos como clases, objetos, herencia, polimorfismo y encapsulamiento es fundamental para desarrollar con Python de manera efectiva.
