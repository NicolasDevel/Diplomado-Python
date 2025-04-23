# Atributos y Métodos en Clases

# Definición de una clase con atributos y métodos
class Persona:
    # Constructor para inicializar atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    # Método para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    # Método para cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"Felicidades, ahora tienes {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Ana", 25)

# Acceso y uso de atributos
print(persona1.nombre)  # Ana
print(persona1.edad)    # 25

# Llamar a métodos
persona1.saludar()      # Hola, mi nombre es Ana y tengo 25 años.
persona1.cumplir_anios()  # Felicidades, ahora tienes 26 años.

# Modificar atributos directamente
persona1.nombre = "María"
persona1.saludar()      # Hola, mi nombre es María y tengo 26 años.

# Ejemplo con atributos de clase
class Animal:
    # Atributo de clase (compartido por todas las instancias)
    reino = "Animalia"

    def __init__(self, especie):
        self.especie = especie  # Atributo de instancia

    def mostrar_info(self):
        print(f"Soy un(a) {self.especie} del reino {Animal.reino}.")

# Crear instancias de la clase Animal
animal1 = Animal("Perro")
animal2 = Animal("Gato")

# Acceso a atributos de instancia y de clase
animal1.mostrar_info()  # Soy un(a) Perro del reino Animalia.
animal2.mostrar_info()  # Soy un(a) Gato del reino Animalia.

# Modificar el atributo de clase
Animal.reino = "Fauna"
animal1.mostrar_info()  # Soy un(a) Perro del reino Fauna.
animal2.mostrar_info()  # Soy un(a) Gato del reino Fauna.

# Modificar atributos de instancia
animal1.especie = "Lobo"
animal1.mostrar_info()  # Soy un(a) Lobo del reino Fauna.
