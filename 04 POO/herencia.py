# Herencia en Python

# Definición de una clase base (o clase padre)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia
        self.tipo = "Desconocido"  # Atributo de instancia

    def saludar(self):
        print(f"Hola, soy un {self.tipo} llamado {self.nombre}.")

# Definición de una clase derivada (o clase hija) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamar al constructor de la clase base (superclase)
        super().__init__(nombre)
        self.tipo = "Perro"  # Sobrescribir el atributo tipo
        self.raza = raza  # Atributo específico de la clase Perro

    # Sobrescribir el método saludar
    def saludar(self):
        super().saludar()  # Llamar al método saludar de la clase base
        print(f"Soy un {self.raza}.")

# Definición de otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, color):
        # Llamar al constructor de la clase base (superclase)
        super().__init__(nombre)
        self.tipo = "Gato"  # Sobrescribir el atributo tipo
        self.color = color  # Atributo específico de la clase Gato

    # Sobrescribir el método saludar
    def saludar(self):
        super().saludar()  # Llamar al método saludar de la clase base
        print(f"Soy de color {self.color}.")

# Crear instancias de las clases derivadas
perro = Perro("Rex", "Labrador")
gato = Gato("Miau", "Blanco")

# Llamar a los métodos sobrescritos
perro.saludar()
gato.saludar()

# Salida esperada:
# Hola, soy un Perro llamado Rex.
# Soy un Labrador.
# Hola, soy un Gato llamado Miau.
# Soy de color Blanco.
