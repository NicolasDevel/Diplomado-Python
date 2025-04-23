# Polimorfismo en Python

# Clase base
class Animal:
    def hablar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

# Subclase 1
class Perro(Animal):
    def hablar(self):
        return "Guau!"

# Subclase 2
class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Subclase 3
class Vaca(Animal):
    def hablar(self):
        return "Muu!"

# Función que recibe un objeto Animal y llama a su método hablar
def hacer_hablar(animal: Animal):
    print(animal.hablar())

# Crear instancias de diferentes tipos de animales
perro = Perro()
gato = Gato()
vaca = Vaca()

# Llamar a la función hacer_hablar con diferentes tipos de objetos
hacer_hablar(perro)  # Salida: Guau!
hacer_hablar(gato)   # Salida: Miau!
hacer_hablar(vaca)   # Salida: Muu!

# El polimorfismo permite que la misma función (hacer_hablar) actúe de manera diferente
# dependiendo del tipo de objeto que se pase como argumento.
