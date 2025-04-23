"""
Un diccionario es una estructura de datos en Python que almacena pares de clave-valor.
Cada clave debe ser única e inmutable (por ejemplo, cadenas, números o tuplas),
mientras que los valores pueden ser de cualquier tipo y repetirse.

Características principales:
- Almacenan datos en pares clave-valor.
- Son mutables: puedes agregar, modificar o eliminar elementos.
- Las claves no pueden repetirse, pero los valores sí.
- El orden de los elementos se mantiene desde Python 3.7.

"""

# Crear un diccionario vacío
diccionario_vacio = {}

# Crear un diccionario con valores
persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero",
    "ciudad": "Bogotá"
}
print(persona)

# Acceder a un valor por su clave
print(persona["nombre"])  # Imprime "Juan"

# Usar el método get para evitar errores si la clave no existe
print(persona.get("pais", "Clave no encontrada"))  # Imprime "Clave no encontrada"

# Agregar una nueva clave-valor
persona["pais"] = "Colombia"
print(persona)

# Modificar un valor existente
persona["edad"] = 31
print(persona)

# Eliminar un elemento por su clave
del persona["ciudad"]
print(persona)

# Otra forma de eliminar con el método pop (devuelve el valor eliminado)
profesion = persona.pop("profesion")
print("Profesión eliminada:", profesion)
print(persona)

# Verificar si una clave existe
print("edad" in persona)  # Devuelve True
print("ciudad" in persona)  # Devuelve False

# Obtener todas las claves, valores y pares clave-valor
print(persona.keys())   # Devuelve las claves
print(persona.values()) # Devuelve los valores
print(persona.items())  # Devuelve pares clave-valor como tuplas

# Recorrer un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Combinar dos diccionarios
otro_diccionario = {"hobby": "Música", "edad": 32}
persona.update(otro_diccionario)
print(persona)  # La clave "edad" será actualizada

# Crear un diccionario a partir de una lista de claves
nuevas_claves = ["clave1", "clave2", "clave3"]
valores_por_defecto = 0
nuevo_diccionario = dict.fromkeys(nuevas_claves, valores_por_defecto)
print(nuevo_diccionario)

# Copiar un diccionario
copia_persona = persona.copy()
print(copia_persona)

# Vaciar un diccionario
persona.clear()
print(persona)  # Diccionario vacío
