"""
Clases y Objetos en Python

Este archivo presenta ejemplos básicos de cómo definir clases, crear objetos e interactuar con ellos.
"""

# Definición de una clase básica
class Coche:
    """
    Clase que representa un coche con atributos básicos.
    """
    def __init__(self, marca, modelo, color):
        """
        Constructor de la clase Coche.
        :param marca: Marca del coche.
        :param modelo: Modelo del coche.
        :param color: Color del coche.
        """
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        """
        Método para simular el arranque del coche.
        """
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        """
        Método para simular que el coche se detiene.
        """
        print(f"El coche {self.marca} {self.modelo} se ha detenido.")

    def mostrar_informacion(self):
        """
        Muestra la información del coche.
        """
        return f"{self.color} {self.marca} {self.modelo}"


# Crear instancias (objetos) de la clase Coche
coche1 = Coche("Toyota", "Corolla", "Rojo")
coche2 = Coche("Ford", "Mustang", "Azul")

# Llamar a métodos de los objetos
coche1.arrancar()
print("Información del coche:", coche1.mostrar_informacion())
coche1.detener()

coche2.arrancar()
print("Información del coche:", coche2.mostrar_informacion())
coche2.detener()

"""
Salida esperada:

El coche Toyota Corolla ha arrancado.
Información del coche: Rojo Toyota Corolla
El coche Toyota Corolla se ha detenido.
El coche Ford Mustang ha arrancado.
Información del coche: Azul Ford Mustang
El coche Ford Mustang se ha detenido.
"""

# Ejemplo adicional: Modificar atributos de un objeto
coche1.color = "Blanco"
print("Nuevo color del coche 1:", coche1.mostrar_informacion())
