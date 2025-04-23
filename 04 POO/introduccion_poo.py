"""
Introducción a la Programación Orientada a Objetos (POO)

La POO es un paradigma de programación que organiza el código en torno a objetos y clases.
Esto permite modelar problemas del mundo real de forma intuitiva y estructurada.
"""

# Ejemplo básico de una clase y un objeto en Python

class Persona:
    """
    Clase Persona para modelar una entidad básica con atributos y métodos.
    """
    def __init__(self, nombre, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """
        Método para que la persona salude.
        """
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")


# Crear un objeto (instancia) de la clase Persona
persona1 = Persona("Ana", 25)

# Acceder a los atributos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")

# Llamar a un método del objeto
persona1.saludar()

"""
Salida esperada:

Nombre: Ana
Edad: 25
Hola, me llamo Ana y tengo 25 años.
"""
